import numpy
import pygame

class triangle:
    PURPLE = (75, 0, 130)
    YELLOW = (255,255,0)
    BLACK = (0, 0, 0)

    def __init__(self, point1, point2, point3,sc):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.sc = sc
        self.isBad = 0

    def dist(self, p, cirX, cirY):
        return numpy.sqrt((cirX - p.x) * (cirX - p.x) + (cirY - p.y) * (cirY - p.y))

    def circumcircleContains(self, p):
        x1 = (self.point1.x + self.point2.x) / 2
        x2 = (self.point2.x + self.point3.x) / 2
        y1 = (self.point1.y + self.point2.y) / 2
        y2 = (self.point2.y + self.point3.y) / 2
        if ((self.point2.y - self.point1.y) == 0) | ((self.point3.y - self.point2.y) == 0):
            cirX = x1
            if ((self.point2.y - self.point1.y) == 0) & ((self.point3.y - self.point2.y) == 0):
                cirY = y1
            elif(self.point2.y - self.point1.y) == 0:
                slope2 = -(self.point3.x - self.point2.x) / (self.point3.y - self.point2.y)
                cirY = slope2 * (cirX - x2) + y2
            else:
                slope1 = -(self.point2.x - self.point1.x) / (self.point2.y - self.point1.y)
                cirY = slope1 * (cirX - x1) + y1
        else:

            slope1 = -(self.point2.x - self.point1.x) / (self.point2.y - self.point1.y)
            slope2 = -(self.point3.x - self.point2.x) / (self.point3.y - self.point2.y)
            if slope1 == slope2:
                print("slope1:", slope1, "slope2:", slope2, "p.x:", p.x, "p.y:", p.y, "point1:", self.point1.x,
                      self.point1.y, "point2:", self.point2.x, self.point2.y, "point3", self.point3.x, self.point3.y)
                return 1
            cirX = (slope1 * x1 - y1 + y2 - slope2 * x2) / (slope1 - slope2 + 10e-6)
            cirY = slope1 * (cirX - x1) + y1
        cirRadius = self.dist(self.point1, cirX, cirY)
        #self.sc.fill(self.BLACK)
        #pygame.draw.circle(self.sc, self.PURPLE, (int(cirX), int(cirY)), int(cirRadius))
        #pygame.draw.circle(self.sc, self.YELLOW, (int(p.x), int(p.y)), 2)
        if cirRadius <= self.dist(p, cirX, cirY):
            return 0
        else:
            return 1

    def contains(self, p):
        if (p == self.point1) | (p == self.point2) | (p == self.point3):
            return True
        else:
            return False
