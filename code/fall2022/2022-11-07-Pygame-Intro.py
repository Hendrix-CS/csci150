# Reminders:
# -- Heap Tracing Homework due on Wednesday


import pygame  # if 'pygame' is underlined, you have to install this library
# to do this, hover your mouse over 'pygame' and select install.
from pygame.locals import * # this lets you have more control

def draw_all(surface):
    surface.fill(pygame.Color(255,255,255))  # what color to use to fill out the background

    # a note on colors:
    # you can specify a color in two ways:
    # ** RGB (Red, Blue, Green), with intensities between 0 and 255, so that
    #       (255,255,255) is white and (0,0,0) is black
    # ** named colors: there are 600+ named colors
    #   see https://www.pygame.org/docs/ref/color_list.html

    #surface.fill(pygame.Color('aqua'))


    # Drawing Objects

    #pygame.draw.<object> will let us draw things!
    # syntax is :
    #pygame.draw.type(what to draw to, color, specific parameters)

    #circles -- syntax is (where, color, (centerx, centery), radius)

    #pygame.draw.circle(surface, pygame.Color(255, 0, 0), (200, 100), 90)


    # rectangles -- syntax is (where, color, (upperleftx, upperlefty, width, height)

   # pygame.draw.rect(surface, pygame.Color(0, 255, 255), (600, 0,100,300))

    # line -- syntax is (where, color, (startx, starty), (endx,endy))
    #pygame.draw.line(surface, pygame.Color(0, 0, 0), (10, 10), (200, 20))

    # you can of course embed them in a loop
    for i in range(1,101,10):
        pygame.draw.circle(surface,pygame.Color(  i,255- i,i),(10+5*i,400-3 * i), i)

    # notice that pygame draws things in order -- the last object will 'cover up' anything drawn first


    pygame.display.update()

def main():
    pygame.init() # this sets up the ability to draw to a window
    surface = pygame.display.set_mode((640, 480)) # 'surface' is the name of the screen
        # where we will draw. We set its size as 640 x 480 pixels;

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True
    while running:
        draw_all(surface) # this is the function which does the drawing
        for event in pygame.event.get(): # this looks at the event queue to see if anything has happened.
            if event.type == QUIT: #'QUIT' is the special pygame operation "I clicked on the close box on the window"
                running = False
    pygame.quit()

#main()


# Pygame can do a lot more than draw -- it can use sound, it can use pre-existing graphics files
# (.jpg, .png, etc) and display them, it can read keyboard and mouse input
#
# We will play with some of these capabilities over the next week


############################################
# Second Example

def draw_all2(surface,offset):
    surface.fill(pygame.Color(255, 255, 255))  # what color to use to fill out the background

    pygame.draw.circle(surface, pygame.Color(255, 0, 0), (100+offset, 100 + 2 * offset), 30)

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
            elif event.type == MOUSEBUTTONDOWN: # notices if the mouse button is clicked!
                offset += 5
    pygame.quit()

main2()