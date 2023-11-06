import pygame
from pygame.locals import *     # Some useful constants

def main():
    pygame.init()    # this sets up the ability to draw to a window
    surface = pygame.display.set_mode((640, 480))
    # 'surface' is the name of the window
    # where we will draw. We set its size to 640 x 480 pixels.

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True

    rect_color = pygame.Color('blue')
    circle_pos = (220, 130)

    i = 0
    while running:
        # i += 1
        # print(f'loop {i}')
        draw_all(surface, rect_color, circle_pos)     # this is the function which does the drawing
        for event in pygame.event.get():   # this looks at the event queue to see if anything has happened.
            if event.type == QUIT:         # 'QUIT' is what happens when the user closes the window
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    running = False
                elif event.key == K_r:
                    rect_color = pygame.Color('red')
                elif event.key == K_p:
                    rect_color = pygame.Color('hotpink4')
                elif event.key == K_b:
                    rect_color = pygame.Color('blue')
                elif event.key == K_DOWN:
                    circle_pos = (circle_pos[0], circle_pos[1] + 10)



    pygame.quit()


def draw_all(surface, rect_color: Color, circle_pos):
    surface.fill(pygame.Color(255, 255, 255))
    # surface.fill(pygame.Color('darkgoldenrod1'))

    # a note on colors:
    # you can specify a color in two ways:
    # ** RGB (Red, Green, Blue), with intensities between 0 and 255, so that
    #       (255,255,255) is white and (0,0,0) is black
    # ** named colors: there are 600+ named colors
    #   see https://www.pygame.org/docs/ref/color_list.html

    # Drawing Objects

    # pygame.draw.<object> will let us draw things!
    pygame.draw.circle(surface, pygame.Color('violet'), circle_pos, 50, width=5)

    pygame.draw.line(surface, pygame.Color('red'), (220, 130), (500, 250))
    pygame.draw.aaline(surface, pygame.Color('red'), (220, 150), (500, 270))

    pygame.draw.rect(surface, rect_color, ((300, 400), (50, 70)))

    pygame.display.update()  # update the window once we're ready


main()
