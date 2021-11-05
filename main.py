# Inspired by Daniel Shiffman Growing Circles coding challenge

import tkinter
import random
import math
from Circle import Circle

# Height and width of our canvas
height = 300
width = 600

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="#333", height=height, width=width)


# simplifies the Tkinter method to create a circle
def _create_circle(c, **kwargs):
    return C.create_oval(c.x - c.r, c.y - c.r, c.x + c.r, c.y + c.r, **kwargs)


C.create_circle = _create_circle

circles = []
tolerance = 0

while len(circles) < 1000:
    # Create a circle of radius 0 at any random spot on our canvas.
    rHeight = random.randrange(0, height)
    rWidth = random.randrange(0, width)
    circ = Circle(rWidth, rHeight, 0)

    touched = False
    inside = False

    # if our circle hasn't touched anything we want to keep working on it
    while not touched:
        # if statement checks to see if our circle is touching any of the edges of our canvas. the reason we do a +2
        # is because that is the width of our line when we draw the circle.
        if circ.x + circ.r > width + 2 or circ.x - circ.r < 2 or circ.y - circ.r < 2 or circ.y + circ.r > height + 2:
            touched = True

        # Compare the current circles distance to any other circle that we're going to draw. if our distance is less
        # than both circles radius, then we know were touching.
        for other in circles:
            dist = math.sqrt(((circ.x - other.x) ** 2) + ((circ.y - other.y) ** 2))
            if dist <= circ.r + other.r:
                touched = True
            # this handles any circles that could spawn inside of an other circle, if the distance is shorter than the
            # radius of another circle, we know the current circle is inside of the other circle.
            if dist <= other.r:
                inside = True

        # if were inside another circle we'll just skip, if we haven't touched another circle lets grow and if we
        # have touched and aren't inside, we can add the current circle to our list of circles
        if inside:
            break
        elif not touched:
            circ.grow()
        else:
            circles.append(circ)

    # tolerance to exit the loop if we cant find any more valid circles.
    tolerance += 1
    if tolerance >= 10000:
        break

# Draw all the circles in circles!
for i in circles:
    C.create_circle(i, outline="#fff", width=2)

C.pack()
top.mainloop()
