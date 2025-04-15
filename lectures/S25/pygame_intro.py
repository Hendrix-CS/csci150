import pygame
from pygame.locals import *     # Some useful constants

def main():
    pygame.init()    # this sets up the ability to draw to a window
    surface = pygame.display.set_mode( (640, 480) )
    # 'surface' is the name of the window
    # where we will draw. We set its size to 640 x 480 pixels.

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True
    # frame = 0
    second_polygon = False
    circle_center = (100, 300)

    while running:
        # frame += 1
        # print(frame)
        circle_center = (circle_center[0] + 1, circle_center[1])
        draw_all(surface, second_polygon, circle_center)     # this is the function which does the drawing
        for event in pygame.event.get():   # this looks at the event queue to see if anything has happened.
            if event.type == QUIT:         # 'QUIT' is what happens when the user closes the window
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_c:
                    second_polygon = not second_polygon
                elif event.key == K_RIGHT:
                    circle_center = (circle_center[0] + 10, circle_center[1])

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

    pygame.draw.circle(surface, 'purple', circle_center, radius=50, width=5)

    pygame.draw.polygon(surface, 'green', [(10,50), (500,90), (300, 240), (200, 380)])
    if second_polygon:
        pygame.draw.polygon(surface, 'saddlebrown', [(40, 50), (530, 90), (330, 240), (230, 380)])

    pygame.display.update()  # update the window once we're ready

main()
