import pygame
from pygame.locals import *     # Some useful constants

def main():
    pygame.init()    # this sets up the ability to draw to a window
    surface = pygame.display.set_mode( (640, 480) )
    # 'surface' is the name of the window
    # where we will draw. We set its size to 640 x 480 pixels.

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True

    while running:
        draw_all(surface)     # this is the function which does the drawing
        for event in pygame.event.get():   # this looks at the event queue to see if anything has happened.
            if event.type == QUIT:         # 'QUIT' is what happens when the user closes the window
                running = False

    pygame.quit()


def draw_all(surface, second_polygon, circle_center):
    surface.fill('white')

    # a note on colors:
    # you can specify a color in two ways:
    # ** RGB (Red, Green, Blue), with intensities between 0 and 255, so that
    #       (255,255,255) is white and (0,0,0) is black
    # ** named colors: there are 600+ named colors
    #   see https://www.pygame.org/docs/ref/color_list.html

    # Drawing Objects
    # pygame.draw.<object> will let us draw things!

    pygame.display.update()  # update the window once we're ready

main()
