class Point:
    """A triangle corner point"""
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def getX(self):
        """Get the x coordinate of the corner point"""
        return self.xCoord

    def getY(self):
        """Get the y coordinate of the corner point"""
        return self.yCoord

    def midPoint(self, otherPoint):
        """Get the midpoint"""
        newX = (self.xCoord + otherPoint.xCoord) / 2
        newY = (self.yCoord + otherPoint.yCoord) / 2
        return Point(newX, newY)
