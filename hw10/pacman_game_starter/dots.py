from dot import Dot


class Dots:
    """A collection of dots."""
    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 50
        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [Dot(self.SPACING * i, self.TH)
                        for i in range(self.WIDTH//self.SPACING + 1)]
        self.bottom_row = [Dot(self.SPACING * i, self.BH)
                           for i in range(self.WIDTH//self.SPACING + 1)]
        self.left_col = [Dot(self.LV, self.SPACING * i)
                         for i in range(self.HEIGHT//self.SPACING + 1)]
        self.right_col = [Dot(self.RV, self.SPACING * i)
                          for i in range(self.HEIGHT//self.SPACING + 1)]

    def display(self):
        """Calls each dot's display method"""
        for i in range(0, len(self.top_row)):
            self.top_row[i].display()
        for i in range(0, len(self.bottom_row)):
            self.bottom_row[i].display()
        for i in range(0, len(self.left_col)):
            self.left_col[i].display()
        for i in range(0, len(self.right_col)):
            self.right_col[i].display()

    # PROBLEM 3: implement dot eating
    # BEGIN CODE CHANGES
    def eat(self, x, y):
        if y == self.TH:
            for dot in self.top_row:
                if abs(x-dot.x) <= self.EAT_DIST:
                    if dot.x == 0 or dot.x == self.WIDTH:
                        self.top_row.pop(0)
                        self.top_row.pop()
                    else:
                        self.top_row.remove(dot)
        if y == self.BH:
            for dot in self.bottom_row:
                if abs(x-dot.x) <= self.EAT_DIST:
                    if dot.x == 0 or dot.x == self.WIDTH:
                        self.bottom_row.pop(0)
                        self.bottom_row.pop()
                    else:
                        self.bottom_row.remove(dot)
        if x == self.LV:
            for dot in self.left_col:
                if abs(y-dot.y) <= self.EAT_DIST:
                    if dot.y == 0 or dot.y == self.WIDTH:
                        self.left_col.pop(0)
                        self.left_col.pop()
                    else:
                        self.left_col.remove(dot)
        if x == self.RV:
            for dot in self.right_col:
                if abs(y-dot.y) <= self.EAT_DIST:
                    if dot.y == 0 or dot.y == self.WIDTH:
                        self.right_col.pop(0)
                        self.right_col.pop()
                    else:
                        self.right_col.remove(dot)
    # END CODE CHANGES

    def dots_left(self):
        """Returns the number of remaing dots in the collection"""
        return (len(self.top_row) +
                len(self.bottom_row) +
                len(self.left_col) +
                len(self.right_col))
