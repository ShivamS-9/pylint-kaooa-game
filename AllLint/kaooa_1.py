import math
import pygame

pygame.init()

WIDTH = 900
HEIGHT = 1000
CIRCLE_RADIUS = 15
LINE = 400
PINK= (255, 192, 203)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gameee")

class Point:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.adjacent = []
        self.double = []
        self.mid = {}

def draw_board(surface):
    x, y = 600, 400
    pygame.draw.line(surface, BLACK, (x, y), (x, y + LINE))
    pygame.draw.line(surface, BLACK, (x, y), (x + LINE*math.cos(math.radians(54)), y + LINE*math.sin(math.radians(54))))
    y = 800
    pygame.draw.line(surface, BLACK, (x, y), (x + LINE*math.cos(math.radians(54)), y - LINE*math.sin(math.radians(54))))
    x += LINE*math.cos(math.radians(54))
    y -= LINE*math.sin(math.radians(54))
    pygame.draw.line(surface, BLACK, (x, y), (x - LINE*math.cos(math.radians(18)), y + LINE*math.sin(math.radians(18))))
    y += LINE*math.sin(math.radians(38))
    pygame.draw.line(surface, BLACK, (x, y), (x - LINE*math.cos(math.radians(18)), y - LINE*math.sin(math.radians(18))))

    points = []
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 2))
    y -= LINE*math.sin(math.radians(38))
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 1))
    x, y = 600, 400
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 0))
    y = 800
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 3))
    y -= LINE*math.sin(math.radians(38))
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 5))
    y = 400 + LINE*math.sin(math.radians(38))
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 9))
    x, y = 600, 400
    x += LINE*math.cos(math.radians(77))
    y += LINE*math.cos(math.radians(72))
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 6))
    y += LINE*math.cos(math.radians(68))
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 8))
    x, y = 600, 400
    x -= LINE*math.cos(math.radians(70))
    y += LINE*math.cos(math.radians(60))
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 4))
    x += 282
    pygame.draw.circle(surface, BLUE, (x,y), CIRCLE_RADIUS)
    points.append(Point(x, y, 7))

    for pt in points:
        if pt.index == 0:
            pt.adjacent.append(5)
            pt.adjacent.append(6)
            pt.double.append(7)
            pt.double.append(9)
            pt.mid[7] = 6
            pt.mid[9] = 5
        
        elif pt.index == 1:
            pt.adjacent.append(6)
            pt.adjacent.append(7)

            pt.double.append(5)
            pt.double.append(8)

            pt.mid[5] = 6
            pt.mid[8] = 7

        elif pt.index == 2:
            pt.adjacent.append(7)
            pt.adjacent.append(8)

            pt.double.append(6)
            pt.double.append(9)

            pt.mid[6] = 7
            pt.mid[9] = 8

        elif pt.index == 3:
            pt.adjacent.append(8)
            pt.adjacent.append(9)

            pt.double.append(5)
            pt.double.append(7)

            pt.mid[5] = 9
            pt.mid[7] = 8

        elif pt.index == 4:
            pt.adjacent.append(5)
            pt.adjacent.append(9)

            pt.double.append(6)
            pt.double.append(8)

            pt.mid[6] = 5
            pt.mid[8] = 9

        elif pt.index == 5:
            pt.adjacent.append(0)
            pt.adjacent.append(4)
            pt.adjacent.append(6)
            pt.adjacent.append(9)

            pt.double.append(1)
            pt.double.append(3)

            pt.mid[1] = 0
            pt.mid[3] = 4

        elif pt.index == 6:
            pt.adjacent.append(0)
            pt.adjacent.append(1)
            pt.adjacent.append(5)
            pt.adjacent.append(7)

            pt.double.append(2)
            pt.double.append(4)

            pt.mid[2] = 7
            pt.mid[4] = 5

        elif pt.index == 7:
            pt.adjacent.append(1)
            pt.adjacent.append(2)
            pt.adjacent.append(6)
            pt.adjacent.append(8)

            pt.double.append(0)
            pt.double.append(3)

            pt.mid[0] = 6
            pt.mid[3] = 8

        elif pt.index == 8:
            pt.adjacent.append(2)
            pt.adjacent.append(3)
            pt.adjacent.append(7)
            pt.adjacent.append(9)

            pt.double.append(1)
            pt.double.append(4)

            pt.mid[1] = 7
            pt.mid[4] = 9

        elif pt.index == 9:
            pt.adjacent.append(3)
            pt.adjacent.append(4)
            pt.adjacent.append(5)
            pt.adjacent.append(8)

            pt.double.append(0)
            pt.double.append(2)

            pt.mid[0] = 5
            pt.mid[2] = 8


    return points

def ponit_dist(x, y, x_0, y_0):
    DIST = (x - x_0)**2 + (y - y_0)**2
    DIST = math.sqrt(DIST)
    return DIST

GAME_OVER = False
PLAYER = '1'
PINK_PT = Point(10000, 10000, 0)
RED_COUNT = 0
RED_POS = []
PN = PINK_PT
COUNT = 0
ULTRA_FLAG = 0
ULTRA_PTLIST = []

screen.fill(WHITE)
points = draw_board(screen)

print("Welcome!")
print("Vulture colour is PINK, CRows clour is Orange")

while not GAME_OVER:
    WIN_FLAG = 0
    if COUNT == 4:
        print("Vulture wins!")
        break
    for num in PINK_PT.adjacent:
        for pt in RED_POS:
            if pt.index == num:
                WIN_FLAG += 1
                break
    if WIN_FLAG != 0 and WIN_FLAG == len(PINK_PT.adjacent):
        print("Crows Win!")
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            xdash, ydash = pygame.mouse.get_pos()
            DIST = 100
            for pt in points:
                if ponit_dist(pt.x, pt.y, xdash, ydash) < DIST:
                    DIST = ponit_dist(pt.x, pt.y, xdash, ydash)
                    PN = Point(pt.x, pt.y, pt.index)
                    PN.adjacent = pt.adjacent
                    PN.double = pt.double
                    PN.mid = pt.mid
            if ULTRA_FLAG == 1:
                for pt in ULTRA_PTLIST:
                    if PN.index == pt.index:
                        pygame.draw.circle(screen, BLUE, (PN.x, PN.y), CIRCLE_RADIUS)
                        pygame.draw.circle(screen, ORANGE, (ultra_PN.x, ultra_PN.y), CIRCLE_RADIUS)
                        for poi in RED_POS:
                            if poi.index == PN.index:
                                RED_POS.remove(poi)
                                break
                        RED_POS.append(ultra_PN)
                    else:
                        pygame.draw.circle(screen, ORANGE, (pt.x, pt.y), 5)
                ULTRA_FLAG = 0
                PLAYER = '2'
                pygame.display.update()
                continue
            FLAG = 0
            for pt in RED_POS:
                if PN.x == pt.x and PN.y == pt.y:
                    FLAG = 1
                    break
            if PN.x == PINK_PT.x and PN.y == PINK_PT.y:
                FLAG = 1
            if PLAYER == '1' and FLAG == 0:
                if RED_COUNT < 7:
                    pygame.draw.circle(screen, ORANGE, (PN.x, PN.y), CIRCLE_RADIUS)
                    RED_COUNT += 1
                    RED_POS.append(PN)
                    PLAYER = '2'
                else:
                    ultra_PN = PN
                    for pt in PN.adjacent:
                        for point in RED_POS:
                            if pt != PINK_PT.index and pt == point.index:
                                pygame.draw.circle(screen, BLUE, (point.x, point.y), 5)
                                ULTRA_PTLIST.append(point)
                    ULTRA_FLAG = 1
            elif PLAYER == '2' and FLAG == 0:
                if PINK_PT.x == 10000 or PN.index in PINK_PT.adjacent:
                    if PINK_PT.x != 10000:
                        pygame.draw.circle(screen, BLUE, (PINK_PT.x, PINK_PT.y), CIRCLE_RADIUS)
                    pygame.draw.circle(screen, PINK, (PN.x, PN.y), CIRCLE_RADIUS)
                    PINK_PT = PN
                    PLAYER = '1'
                elif PN.index in PINK_PT.double:
                    for res in RED_POS:
                        if res.index == PINK_PT.mid[PN.index]:
                            pygame.draw.circle(screen, BLUE, (PINK_PT.x, PINK_PT.y), CIRCLE_RADIUS)
                            pygame.draw.circle(screen, PINK, (PN.x, PN.y), CIRCLE_RADIUS)
                            COUNT += 1
                            pygame.draw.circle(screen, BLUE, (res.x, res.y), CIRCLE_RADIUS)
                            RED_POS.remove(res)
                            PINK_PT = PN
                            PLAYER = '1'
                            break
        pygame.display.update()
    pygame.display.flip()
pygame.quit()

