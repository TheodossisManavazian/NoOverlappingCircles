class Circle:
    x = 0
    y = 0
    r = 0
    growing = True

    def __init__(self, x_, y_, r_):
        self.x = x_
        self.y = y_
        self.r = r_

    def pt(self):
        print(self.x, self.y, self.r)

    def grow(self):
        self.r += .2
