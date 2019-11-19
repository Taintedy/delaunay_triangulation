
import pygame
from delaunay import delaunay
from points import point
import random



FPS = 144
WIN_WIDTH = 1500
WIN_HEIGHT = 1000
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (75, 0, 130)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
pygame.init()

clock = pygame.time.Clock()
points = []

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

points.sort(key=lambda p: p.x)

while 1:
    sc.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            for l in points:
                print("point(", l.x, ",", l.y, "),")
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:
                tempMousePos = pygame.mouse.get_pos()
                points.append(point(tempMousePos[0], tempMousePos[1]))
                for i in range(0, len(points)):
                    for j in range(i + 1, len(points)):
                        if points[i].theSame(points[j]):
                            points.remove(points[j])
                for l in range(0, len(points) - 1):
                    for j in range(0, len(points) - 1):
                        if points[j + 1].x < points[j].x:
                            temp = points[j]
                            points[j] = points[j + 1]
                            points[j + 1] = temp


    if len(points) != 0:
        delaun = delaunay(points, sc)
    pygame.display.update()
    clock.tick(FPS)
