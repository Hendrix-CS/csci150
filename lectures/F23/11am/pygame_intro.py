import pygame
from pygame.locals import *     # Some useful constants

def main():
    pygame.init()    # this sets up the ability to draw to a window
    surface = pygame.display.set_mode((640, 480))
    # 'surface' is the name of the window
    # where we will draw. We set its size to 640 x 480 pixels.

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True

    rect_blue = pygame.Color('mediumpurple4').b
    circle_pos = (130, 200)

    while running:
        draw_all(surface, rect_blue, circle_pos)     # this is the function which does the drawing
        for event in pygame.event.get():   # this looks at the event queue to see if anything has happened.
            if event.type == QUIT:         # 'QUIT' is what happens when the user closes the window
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                rect_blue = (rect_blue + 20) % 256
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    running = False
                elif event.key == K_DOWN:
                    circle_pos = (circle_pos[0], circle_pos[1] + 20)


    pygame.quit()


def draw_all(surface, rect_blue, circle_pos):
    surface.fill(pygame.Color(255, 255, 255))
    # surface.fill(pygame.Color('darkgreen'))

    # a note on colors:
    # you can specify a color in two ways:
    # ** RGB (Red, Green, Blue), with intensities between 0 and 255, so that
    #       (255,255,255) is white and (0,0,0) is black
    # ** named colors: there are 600+ named colors
    #   see https://www.pygame.org/docs/ref/color_list.html

    # Drawing Objects

    # pygame.draw.<object> will let us draw things!

    pygame.draw.circle(surface, pygame.Color('purple'), circle_pos, 50, width=10)

    vertices = [(5,100), (17, 36), (200, 80)]
    pygame.draw.polygon(surface, pygame.Color('darkgoldenrod3'), vertices)

    pygame.draw.line(surface, pygame.Color('black'), (200, 100), (250, 200), width=3)

    med_purple = pygame.Color('mediumpurple4')
    pygame.draw.rect(surface, pygame.Color(med_purple.r, med_purple.g, rect_blue), ((400, 300), (50, 100)))


    pygame.display.update()  # update the window once we're ready


main()
