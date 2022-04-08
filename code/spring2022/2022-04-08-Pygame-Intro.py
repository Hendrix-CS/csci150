import pygame
from pygame.locals import * # this lets you have more control

def draw_all(surface):
    surface.fill(pygame.Color(255,255,255))  # what color to use to fill out the background

    #pygame.draw.<object> will let us draw things!
    # syntax is :
    #pygame.draw.type(what to draw to, color, specific parameters)

    #circles -- syntax is (where, color, (centerx, centery), radius)


    # pygame.draw.circle(surface, pygame.Color(150, 200, 0), (150, 100), 60)
    #
    # pygame.draw.circle(surface, pygame.Color(255, 0, 0), (200, 100), 90)

    # rectangles -- syntax is (where, color, (upperleftx, upperlefty, width, height)

    #pygame.draw.rect(surface, pygame.Color(0, 255, 255), (200, 0,100,500))

    # line -- syntax is (where, color, (startx, starty), (endx,endy))
    # pygame.draw.line(surface, pygame.Color(0, 0, 0), (10, 10), (200, 20))

    # for i in range(1,101,10):
    #     pygame.draw.circle(surface,pygame.Color(  i,255- i,i),(10+i,200-3 * i), i)


    pygame.display.update()


def main():
    pygame.init() # this sets up the ability to draw to a window
    surface = pygame.display.set_mode((640, 600)) # 'surface' is the name of the screen
        # where we will draw. We set its size as 640 x 480 pixels;

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True
    while running:
        draw_all(surface) # this is the function which does the drawing
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    pygame.quit()


# if __name__ == '__main__':
#     main()

def draw_all2(surface,offset):
    surface.fill(pygame.Color(255, 255, 255))  # what color to use to fill out the background

    pygame.draw.circle(surface, pygame.Color(255, offset, offset), (100+offset, 100 + 2 * offset), 30)

    pygame.display.update()


def main2():
    pygame.init() # this sets up the ability to draw to a window
    surface = pygame.display.set_mode((640, 480)) # 'surface' is the name of the screen
        # where we will draw. We set its size as 640 x 480 pixels;
    offset = 0
    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True
    while running:
        draw_all2(surface,offset) # this is the function which does the drawing
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                offset += 5
    pygame.quit()

main2()