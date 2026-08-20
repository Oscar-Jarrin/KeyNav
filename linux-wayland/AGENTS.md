# KeyNav (Linux/Wayland) — Project Blueprint & Collaboration Guide

## Project Vision

KeyNav is a Linux desktop application that lets a user drive the mouse and
other system-level actions entirely from the keyboard. This directory is the
Wayland-native rewrite of the original Windows prototype (see `../windows`),
built on `evdev` for input and `uinput` for output instead of a
higher-level, X11-only library like `pynput`.

This is a **portfolio project**. The measure of success is not just "does it
work" but:

- The architecture is understandable by a stranger reading the code once.
- Each layer (input, processing, output, UI) can be tested or replaced in
  isolation.
- The author (the human in this repo) can explain *why* every non-trivial
  decision was made — not just paste working code.

the agent's job here is closer to **technical mentor** than **code generator**.
Correctness matters, but comprehension is the actual deliverable.

## Architectural Blueprint

KeyNav is event-driven, built around four decoupled layers connected by an
internal **Event Bus** (Pub/Sub). No layer should import or directly call
into another layer's internals — they only publish and subscribe to events.

```
┌───────────────┐     raw events      ┌───────────────┐
│  evdev Reader  │ ──────────────────▶ │               │
└───────────────┘                     │               │      ┌───────────────┐
                                       │   Event Bus    │◀────▶│      GUI      │
┌───────────────┐   synthetic events  │  (Pub/Sub)     │      └───────────────┘
│ uinput Writer  │ ◀────────────────── │               │
└───────────────┘                     └───────┬───────┘
                                               │
                                       ┌───────▼───────┐
                                       │  Processing /  │
                                       │  State Layer   │
                                       └───────────────┘
```

- **evdev Reader** — Opens device node(s) under `/dev/input/`, reads raw
  `InputEvent`s, and *publishes* them onto the bus as normalized domain
  events (e.g. `KeyDown(code)`, `KeyUp(code)`). It knows nothing about what
  those keys *mean*.
- **Processing / State Layer** — Subscribes to normalized input events,
  maintains the current mode/state (e.g. "mouse navigation mode" vs.
  "transparent mode"), and decides what should happen. It *publishes*
  intent events like `MoveCursor(dx, dy)` or `ClickButton(LEFT)`. It never
  touches `evdev` or `uinput` directly — that's what keeps it testable
  without real hardware.
- **uinput Writer** — Subscribes to intent events and translates them into
  synthetic input by writing to a virtual `uinput` device. It knows nothing
  about *why* a click happened, only how to emit one.
- **GUI** — Subscribes to state-change events to reflect what mode KeyNav is
  in, and publishes configuration-change events (e.g. rebinding a key) back
  onto the bus. The processing layer must work correctly with **no GUI
  running at all** — the GUI is an observer/controller, not a dependency.

Rule of thumb: if you find yourself wanting to import `evdev` or `uinput`
inside the processing layer, or inside the GUI, that's a sign the event bus
contract is being bypassed and needs to be fixed instead of worked around.

## Permissions & Security

`evdev` (reading `/dev/input/event*`) and `uinput` (writing to
`/dev/uinput`) both require elevated access on a stock Linux system. This
project must **never** default to "just run it as root."

Guidelines:

- **Prefer group-based access over root.** The standard approach is to add
  the user to the `input` group (for reading `/dev/input/event*`) and to
  install a `udev` rule granting the `input` group (or a dedicated
  `uinput` group) read/write access to `/dev/uinput`. Document the exact
  `udev` rule and `usermod` command in the repo's setup instructions rather
  than telling the user to `sudo` the app itself.
- **Never silently escalate privileges** (no embedded `sudo`, no setuid
  binaries) without the user explicitly asking for and understanding that
  tradeoff. If elevated access is genuinely unavailable, fail loudly with a
  clear error message and a pointer to the udev/group setup, not a silent
  fallback.
- **Principle of least privilege applies to device scope too.** Grab only
  the specific input device(s) needed (e.g. keyboard event nodes), not a
  blanket read of all `/dev/input/*`. When using `EVIOCGRAB` to take
  exclusive control of a device, be explicit in code and comments about why
  — grabbing a device makes it invisible to the rest of the system while
  held, which is a real usability/safety tradeoff worth flagging to the
  user before implementing.
- **Treat the virtual `uinput` device as a trust boundary.** Anything that
  can write to it can synthesize arbitrary keyboard/mouse input system-wide.
  Config files that map physical keys to synthetic actions should be
  validated, not `eval`'d or otherwise executed.
- Do not commit udev rules or setup scripts that assume a specific
  username/UID — they should be generic and reviewed before being added.

## Learning Mandate (how Claude must operate in this project)

This project exists so the user can learn the "why," not just get to
"it runs." When assisting in this directory, Claude **must**:

1. **Never drop large blocks of code without explaining the mechanism
   first.** Before writing an `evdev` read loop, a `uinput` device
   registration, or an event bus dispatch, explain in plain terms what is
   happening at the syscall/library level and why it's structured that way.
   Prefer small, incremental snippets the user can absorb over a full file
   dump.
2. **Always surface architectural trade-offs explicitly**, don't just pick
   one silently. At minimum, this means calling out things like:
   - Threading vs. `asyncio` for the event bus and the `evdev` read loop.
   - Blocking reads vs. polling (`select`/`epoll`) on the evdev file
     descriptor.
   - Synchronous in-process pub/sub vs. a queue-based bus (thread-safety
     implications when the GUI runs on its own thread/loop).
   When one option is clearly better for this project's goals, say so and
   say why — but the reasoning must be visible, not assumed.
3. **Ask prompting questions before advancing.** Before moving to the next
   implementation step, check the user's understanding of the current one
   (e.g. "Before we wire the uinput writer to the bus — what do you expect
   happens if two events are published faster than the writer can consume
   them?"). Don't treat silence/agreement as understanding; prefer a
   question that would expose a misconception if one exists.
4. **Prioritize a working mental model over a working program.** If asked
   to "just make it work," it's appropriate to push back gently and offer
   the explained path first, unless the user explicitly says they want to
   move fast and skip the explanation for that particular step.

## Tech Stack Recommendations

### GUI framework

| Option | Pros | Cons |
|---|---|---|
| **PySide6** (Qt bindings) | Native Wayland support out of the box; signals/slots map almost 1:1 onto a pub/sub event bus, which is great for teaching the pattern; mature, well-documented; easy to run a Qt event loop alongside `asyncio` via `qasync`. | Heavier dependency; PyQt6 licensing (GPL/commercial) vs. PySide6 (LGPL) is worth understanding, not just picking blindly. |

Recommendation: **PySide6** is the best fit here — Wayland support is solid, its signal/slot system is a production-grade example of the exact pub/sub pattern KeyNav is built around, and comparing "Qt's built-in event system" to "our own event bus" is a good learning contrast.

### Event Bus approach

We are going to use pyqt5 sockets
