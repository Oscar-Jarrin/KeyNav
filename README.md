# KeyPolarNav
A program that allows you to use your cursor, and other mouse/keyboard functions using our keyboard based on the idea of using some kind of keys to polar coordinates projected on the screen

A little sketch of how it can work, and the functions it could have:
    click function:
        open click mode: {determine a combination to open the click mode}
            radius selection:
                a set of 8 possible radius with values between [a=0, ñ=max], being max the distance between the centre of the screen and the "X"(close) button, and obviously, 
                the minimmum would be the centre of your screen. The rest of the radius will be values interpolated according to the size of your screen
            radius refinement:
                once the base radius is set, you can decide wether the radius starts increasing towards the next value (with h) and stop (with h) and then select the angle. 
                or decrease the radius (with g) and stop (with g)
            angle selction:
                angle sign:
                    once the radius is selected, select a sign for the angles positive or negative to determine if you're gonna use the top or bot part of the screen.  
                angle magnitude:
                    once you set the sign of the angle you select the magnitude of the angle between 8 possible values with 8 different keys
                    a = 7π/8, s = 6π/8 == 3π/4, d = 5π/8, f = 4π/8 == π/2, j = 3π/8, k = 2π/8 == π/4, l = π/8, ñ = 0
            angle refinement:
                once the gase angle is set, you can decide wether the angle starts "increasing towards the next value" (with h) and stop (with h) and then select the angle. 
                or "decrease" the radius (with g) and stop (with g)
                NOTE: for pruposes of usability, I will define:
                    increasing an angle: the magnitude of the angle will decrease if it is <= π/2
                    decreasing an angle: the magnitude of the angle will increase if it is >= π/2
                    this way I think will be more intuitive to use so if I press "h", the angle will move to the right, and if I press "g" it'll move to the left, 
                    making it similar to the radius behaviour.
            click determination 
                j for left click
                k for middle click
                l for right click
    scroll function: {determine a combination to open the scroll mode}
        open scroll function:

    drag & drop function: {determine a combination to open the drag and drop function}
        open drag & drop function:
    