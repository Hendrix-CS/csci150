import pygame
from pygame.locals import * # this lets you have more control

# Reminders
# Final Project Design Document Due Friday





#########################
# PyGame is a libray that:
#  * Allows us to draw shapes on a window!
#  * Detects keyboard and mouse input
#  * can also play sound
#  * display image files

# When you use this file, at the top, you see:

# import pygame
# from pygame.locals import * # this lets you have more control

# Likely, the pygame is underlined in red
# Hover over the word pygame and choose 'Install Package pygame'
# The red should disappear!



def draw_all(surface):
    surface.fill(pygame.Color(255,255,255))  # what color to use to fill out the background


    #pygame.draw.<object> will let us draw things!
    # syntax is :
    #pygame.draw.type(what to draw to, color, specific parameters)

    #circles -- syntax is (where, color, (centerx, centery), radius)



    # #

    pygame.draw.circle(surface, pygame.Color(0,255,0), (400,400), 300)
    pygame.draw.circle(surface, pygame.Color(50, 0, 200), (500, 600), 20)

    #
    # # rectangles -- syntax is (where, color, (upperleftx, upperlefty, width, height)
    #
    pygame.draw.rect(surface, pygame.Color(0, 255, 255), (600, 0,100,300))


    #
    # # line -- syntax is (where, color, (startx, starty), (endx,endy))
    pygame.draw.line(surface, pygame.Color(0, 0, 0), (10, 10), (200, 20))
    #
    for i in range(1,101,10):
        pygame.draw.circle(surface,pygame.Color(  i,255- i,i),(10+i,200-3 * i), i)
    #

    pygame.display.update()


def main():
    pygame.init() # this sets up the ability to draw to a window
    surface = pygame.display.set_mode((1000, 800)) # 'surface' is the name of the screen
        # where we will draw. We set its size as 1000 x 800 pixels;

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True
    while running:
        draw_all(surface) # this is the function which does the drawing
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    pygame.quit()

#main()


def draw_all2(surface,offset):
    surface.fill(pygame.Color(255, 255, 255))  # what color to use to fill out the background

    pygame.draw.circle(surface, pygame.Color(255,0,0), (100+offset, 100 + 2 * offset), 30 + offset)

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
            elif event.type == KEYDOWN:
                        if event.key ==K_LEFT:
                            offset -= 25
                        elif event.key == K_RIGHT:
                            offset += 30
    pygame.quit()

main2()