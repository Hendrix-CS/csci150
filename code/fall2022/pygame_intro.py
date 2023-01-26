import pygame
from pygame.locals import *     # Some useful constants

def main():
    pygame.init()    # this sets up the ability to draw to a window
    surface = pygame.display.set_mode((640, 480))
    # 'surface' is the name of the window
    # where we will draw. We set its size to 640 x 480 pixels.

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True
    xoffset: int = 0
    yoffset: int = 0
    blue_offset: int = 0
    count = 0
    while running:
        count += 1
        draw_all(surface, xoffset, yoffset, blue_offset)     # this is the function which does the drawing
        for event in pygame.event.get():   # this looks at the event queue to see if anything has happened.
            if event.type == QUIT:         # 'QUIT' is what happens when the user closes the window
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                xoffset += 5
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    running = False
                elif event.key == K_SPACE:
                    yoffset -= 5
                    print(count)
                    count = 0
                elif event.key == K_b:
                    blue_offset += 15
                    print(count)
                    count = 0

    pygame.quit()


def draw_all(surface, xoffset: int, yoffset: int, blue_offset: int):
    surface.fill(pygame.Color(255, 255, 255))

    # a note on colors:
    # you can specify a color in two ways:
    # ** RGB (Red, Green, Blue), with intensities between 0 and 255, so that
    #       (255,255,255) is white and (0,0,0) is black
    # ** named colors: there are 600+ named colors
    #   see https://www.pygame.org/docs/ref/color_list.html

    # surface.fill(pygame.Color('aqua'))

    # Drawing Objects

    # pygame.draw.<object> will let us draw things!

    pygame.draw.circle(surface, pygame.Color(220, 208, (255 + blue_offset) % 256), (300 + xoffset, 100 + yoffset), 50, width=10)

    pygame.draw.rect(surface, pygame.Color('fuchsia'), (100, 200, 50, 80))  # (x, y, width, height)

    pygame.draw.line(surface, pygame.Color('blue'), (0, 0), (90, 400), width=5)

    for x in range(10):
        pygame.draw.line(surface, pygame.Color('red'), (0, 0), (x*10, 100))

    pygame.display.update()


main()
