import pygame
import math
from pygame import *
from flyobj import *
from math import *

# задаем размеры окна
WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

SPACE_COLOR = "#000022"
SUN_COLOR = "yellow"

# Условие остановки
CRASH_DIST = 10
OUT_DIST = 1000


def main():
    # PyGame init
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Solar")

    # Space init
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(SPACE_COLOR))
    draw.circle(bg, Color(SUN_COLOR), (X0, Y0), 30)

    # Timer init
    timer = pygame.time.Clock()

    # Planet init


    Jupiter = Surface((20, 20))
    Jupiter.fill(Color(SPACE_COLOR))
    draw.circle(Jupiter, Color("#BCBC42"), (20 // 2, 20 // 2), 10)

    Saturn = Surface((20, 20))
    Saturn.fill(Color(SPACE_COLOR))
    draw.circle(Saturn, Color("#6F6F29"), (20 // 2, 20 // 2), 9)

    Uran = Surface((10, 10))
    Uran.fill(Color(SPACE_COLOR))
    draw.circle(Uran, Color("#6AF0EA"), (10 // 2, 10 // 2), 5)

    Neptun = Surface((8, 8))
    Neptun.fill(Color(SPACE_COLOR))
    draw.circle(Neptun, Color("#4262D9"), (8 // 2, 8 // 2), 4)


    jup = FlyObject(int(20), float(160.0), float(300.0), float(1.2),  float(1.8))
    sat = FlyObject(int(18), float(140.0), float(300.0), float(1.2), float(1.8))
    uran = FlyObject(int(14), float(120.0), float(300.0), float(1), float(1.8))
    nept = FlyObject(int(17), float(100.0), float(300.0), float(1), float(1.8))

    done = False
    while not done:
        timer.tick(50)
        for e in pygame.event.get():
            if e.type == QUIT:
                done = True
                break


        r5 = jup.calc()
        r6 = sat.calc()
        r7 = uran.calc()
        r8 = nept.calc()

        screen.blit(bg, (0, 0))

        screen.blit(Jupiter, (int(jup.x), int(jup.y)))
        screen.blit(Saturn, (int(sat.x), int(sat.y)))
        screen.blit(Uran, (int(uran.x), int(uran.y)))
        screen.blit(Neptun, (int(nept.x), int(nept.y)))
        pygame.display.update()



if __name__ == "__main__":
    main()
