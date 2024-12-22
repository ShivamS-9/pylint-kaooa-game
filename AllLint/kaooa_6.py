"""
This is Kaooa game linting
"""

import math
import pygame

pygame.init()
WIDTH = 900
HEIGHT = 1000
CIRCLE_RADIUS = 15
LINE = 400
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPEED = 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gameee")


class Point:
    """
    This is class for point
    """

    def __init__(self, p_x, p_y, index):
        self.x = p_x
        self.y = p_y
        self.index = index
        self.adjacent = []
        self.double = []
        self.mid = {}


def draw_board(surface):
    """
    This is the drawboard func
    """
    my_x, my_y = 600, 400
    pygame.draw.line(surface, BLACK, (my_x, my_y), (my_x, my_y + LINE))
    pygame.draw.line(
        surface,
        BLACK,
        (my_x, my_y),
        (
            my_x + LINE * math.cos(math.radians(54)),
            my_y + LINE * math.sin(math.radians(54)),
        ),
    )
    my_y = 800
    pygame.draw.line(
        surface,
        BLACK,
        (my_x, my_y),
        (
            my_x + LINE * math.cos(math.radians(54)),
            my_y - LINE * math.sin(math.radians(54)),
        ),
    )
    my_x += LINE * math.cos(math.radians(54))
    my_y -= LINE * math.sin(math.radians(54))
    pygame.draw.line(
        surface,
        BLACK,
        (my_x, my_y),
        (
            my_x - LINE * math.cos(math.radians(18)),
            my_y + LINE * math.sin(math.radians(18)),
        ),
    )
    my_y += LINE * math.sin(math.radians(38))
    pygame.draw.line(
        surface,
        BLACK,
        (my_x, my_y),
        (
            my_x - LINE * math.cos(math.radians(18)),
            my_y - LINE * math.sin(math.radians(18)),
        ),
    )
    points = []
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 2))
    my_y -= LINE * math.sin(math.radians(38))
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 1))
    my_x, my_y = 600, 400
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 0))
    my_y = 800
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 3))
    my_y -= LINE * math.sin(math.radians(38))
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 5))
    my_y = 400 + LINE * math.sin(math.radians(38))
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 9))
    my_x, my_y = 600, 400
    my_x += LINE * math.cos(math.radians(77))
    my_y += LINE * math.cos(math.radians(72))
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 6))
    my_y += LINE * math.cos(math.radians(68))
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 8))
    my_x, my_y = 600, 400
    my_x -= LINE * math.cos(math.radians(70))
    my_y += LINE * math.cos(math.radians(60))
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 4))
    my_x += 282
    pygame.draw.circle(surface, BLUE, (my_x, my_y), CIRCLE_RADIUS)
    points.append(Point(my_x, my_y, 7))
    for p_t in points:
        if p_t.index == 0:
            p_t.adjacent.append(5)
            p_t.adjacent.append(6)
            p_t.double.append(7)
            p_t.double.append(9)
            p_t.mid[7] = 6
            p_t.mid[9] = 5
        elif p_t.index == 1:
            p_t.adjacent.append(6)
            p_t.adjacent.append(7)
            p_t.double.append(5)
            p_t.double.append(8)
            p_t.mid[5] = 6
            p_t.mid[8] = 7
        elif p_t.index == 2:
            p_t.adjacent.append(7)
            p_t.adjacent.append(8)
            p_t.double.append(6)
            p_t.double.append(9)
            p_t.mid[6] = 7
            p_t.mid[9] = 8
        elif p_t.index == 3:
            p_t.adjacent.append(8)
            p_t.adjacent.append(9)
            p_t.double.append(5)
            p_t.double.append(7)
            p_t.mid[5] = 9
            p_t.mid[7] = 8
        elif p_t.index == 4:
            p_t.adjacent.append(5)
            p_t.adjacent.append(9)
            p_t.double.append(6)
            p_t.double.append(8)
            p_t.mid[6] = 5
            p_t.mid[8] = 9
        elif p_t.index == 5:
            p_t.adjacent.append(0)
            p_t.adjacent.append(4)
            p_t.adjacent.append(6)
            p_t.adjacent.append(9)
            p_t.double.append(1)
            p_t.double.append(3)
            p_t.mid[1] = 0
            p_t.mid[3] = 4
        elif p_t.index == 6:
            p_t.adjacent.append(0)
            p_t.adjacent.append(1)
            p_t.adjacent.append(5)
            p_t.adjacent.append(7)
            p_t.double.append(2)
            p_t.double.append(4)
            p_t.mid[2] = 7
            p_t.mid[4] = 5
        elif p_t.index == 7:
            p_t.adjacent.append(1)
            p_t.adjacent.append(2)
            p_t.adjacent.append(6)
            p_t.adjacent.append(8)
            p_t.double.append(0)
            p_t.double.append(3)
            p_t.mid[0] = 6
            p_t.mid[3] = 8
        elif p_t.index == 8:
            p_t.adjacent.append(2)
            p_t.adjacent.append(3)
            p_t.adjacent.append(7)
            p_t.adjacent.append(9)
            p_t.double.append(1)
            p_t.double.append(4)
            p_t.mid[1] = 7
            p_t.mid[4] = 9
        elif p_t.index == 9:
            p_t.adjacent.append(3)
            p_t.adjacent.append(4)
            p_t.adjacent.append(5)
            p_t.adjacent.append(8)
            p_t.double.append(0)
            p_t.double.append(2)
            p_t.mid[0] = 5
            p_t.mid[2] = 8
    return points


def ponit_dist(x_ini, y_ini, x_0, y_0):
    """
    This is distance formula docstring
    """
    dis_tance = (x_ini - x_0) ** 2 + (y_ini - y_0) ** 2
    dis_tance = math.sqrt(dis_tance)
    return dis_tance


GAME_OVER = False
PLAYER = "1"
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
                        pygame.draw.circle(
                            screen, ORANGE, (ultra_PN.x, ultra_PN.y), CIRCLE_RADIUS
                        )
                        for poi in RED_POS:
                            if poi.index == PN.index:
                                RED_POS.remove(poi)
                                break
                        RED_POS.append(ultra_PN)
                    else:
                        pygame.draw.circle(screen, ORANGE, 
                        (pt.x, pt.y), 5)
                ULTRA_FLAG = 0
                PLAYER = "2"
                pygame.display.update()
                continue
            FLAG = 0
            for pt in RED_POS:
                if PN.x == pt.x and PN.y == pt.y:
                    FLAG = 1
                    break
            if PN.x == PINK_PT.x and PN.y == PINK_PT.y:
                FLAG = 1
            if PLAYER == "1" and FLAG == 0:
                if RED_COUNT < 7:
                    pygame.draw.circle(screen, ORANGE,
                    (PN.x, PN.y), CIRCLE_RADIUS)
                    RED_COUNT += 1
                    RED_POS.append(PN)
                    PLAYER = "2"
                else:
                    ultra_PN = PN
                    for pt in PN.adjacent:
                        for point in RED_POS:
                            if pt != PINK_PT.index and \
                                pt == point.index:
                                pygame.draw.circle(screen, 
                                BLUE, (point.x, point.y), 5)
                                ULTRA_PTLIST.append(point)
                    ULTRA_FLAG = 1
            elif PLAYER == "2" and FLAG == 0:
                if PINK_PT.x == 10000 or PN.index in PINK_PT.adjacent:
                    if PINK_PT.x != 10000:
                        pygame.draw.circle(
                            screen, BLUE, (PINK_PT.x, PINK_PT.y), CIRCLE_RADIUS
                        )
                    pygame.draw.circle(screen, PINK, (PN.x, PN.y), CIRCLE_RADIUS)
                    PINK_PT = PN
                    PLAYER = "1"
                elif PN.index in PINK_PT.double:
                    for res in RED_POS:
                        if res.index == PINK_PT.mid[PN.index]:
                            pygame.draw.circle(
                                screen, BLUE, (PINK_PT.x, PINK_PT.y), CIRCLE_RADIUS
                            )
                            pygame.draw.circle(
                                screen, PINK, (PN.x, PN.y), CIRCLE_RADIUS
                            )
                            COUNT += 1
                            pygame.draw.circle(
                                screen, BLUE, (res.x, res.y), CIRCLE_RADIUS
                            )
                            RED_POS.remove(res)
                            PINK_PT = PN
                            PLAYER = "1"
                            break
        pygame.display.update()
    pygame.display.flip()
pygame.quit()
