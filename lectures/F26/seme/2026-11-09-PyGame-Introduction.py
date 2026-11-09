# Reminders
# * Final Project Design Document Due Next Monday
# * Quiz #10 Friday (Classes)

# * There us *NOT* a quiz for this week's material (just lab)

# PyGame -- a library which allows you to:
# * Draw shapes on a window
# * Add in .jpeg and other images
# * Detect keyboard/mouse input
# * Play sounds
#
# Official Documentation:
# * https://www.pygame.org/docs/
#
# For the Final Project:
# * You do not need to cite any code you use/modify from class/lab
# * You do not need to cite any assistance you get from
#     * Me
#     * Dr. Delavan, Dr. Ferrer, or Dr. Yorgey
#     * Lab/Help Center TAs
# * Official PyGame (or Python) documentation
# BUT MUST Cite anything else

# The PyGame Library
# Each time you make a new project that uses PyGame, you'll need to:

# hover over the red underlined pygame
# try to install package (this likely will not work)

# then try:
# open settings and choose 'Interpreter'
# Click on the '+' symbol
# enter 'pygame-ce' in the search bar
# install

# if that did not work, try:
# * Open the Terminal
#     - Click on the rectangle that looks like >_
# * type pip install pygame-ce
# Try this *NOW* -- if this does not work, let me know!

from dataclasses import dataclass
import pygame
from pygame.locals import *
import random

# Overview of how we'll use PyGame
# Set-Up
#


# pygame.init()
# surface = pygame.display.set_mode((640, 400))
# surface.fill(pygame.Color(255, 255, 255))

# * Initialize PyGame
# * Build a window, called 'surface', 640 pixels wide, 400 tall
#      (Note: The top left corner is (0,0)
#           - x increases to the right
#           - y increases down
# * Sets the initial background color of the window
#   -- you can use a "named" color: 'black, 'white', 'red', ...
#       or RGB values

# We then have a loop: while running:
# This acts like the frame-builder
# -- you will have *ONE* draw function
# -- the event queue
# -- make any adjustments to the state

# Simple Example:
# #
# def draw_all(surface):
#     pygame.draw.circle(surface, 'red', (300, 150), 75)
#
#     pygame.display.update()
#
#
# def main():
#     pygame.init()
#     surface = pygame.display.set_mode((640, 400))
#     surface.fill(pygame.Color(255, 255, 255))
#     running = True
#     while running:
#         draw_all(surface)
#
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 running = False
#     pygame.quit()
#
# main()

############
# Full Example -- We will talk about each of these pieces
# today and on Wednesday

# This is explicitly designed to allow you to copy and paste and adjust
# as you need for your Final Project
############

# How to draw shapes
# How to put text onto the screen
# How to 'blit' images to the screen
# How to play sounds
# Keyboard input
# Mouse clicks

# Shapes:

# pygame.draw.circle(where, color, (centerx, centery), radius)
# pygame.draw.rect(where, color, (topleftx, toplefty, wdith, height))
# pygame.draw.line(where, color, (startx,starty),(endx,endy))

# Text:
# this is how I format the text that will be printed as the score
def set_text(string, coordx, coordy, fontSize): # Function to set text
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text = font.render(string, True, (0,0,255))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)
#
# # In the draw_all function:
# #     totalText = set_text(score, 20,30, 30)
# #     surface.blit(totalText[0], totalText[1])
#
# # Adding images
# # im = pygame.image.load(image_file)
# # surface.blit(im, (wherex, wherey))
#
#
#
#
@dataclass
class Circle:


    x: int
    y: int
    radius: int
    color: str

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self,x):
        self.x += x

    def new_color(self):
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


def draw_all(surface, score, im,c):
    surface.fill('white') # 'blank' the screen with basic background each time

    # Draw some shapes
    c.draw(surface)
    pygame.draw.rect(surface, 'green', (500,200,50,100))


    # Add some text
    totalText = set_text(score, 350,30, 30)
    surface.blit(totalText[0], totalText[1])

    # Add an image:
    surface.blit(im, (100,100))


    # This needs to be the final line of draw_all -- and only should appear *ONCE*
    pygame.display.update()

def hit(x: int, y: int, c: 'Circle') -> bool:
    if (x - c.x) ** 2 + (y - c.y) ** 2 <= c.radius ** 2:
        return True
    else:
        return False


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))
    surface.fill(pygame.Color(255, 255, 255))

    my_sound = pygame.mixer.Sound('tos_photon_torpedo.mp3')

    score = 0
    im = pygame.image.load('enterprise.jpg')

    c = Circle(50,25,20,'red')

    running = True
    while running:
        draw_all(surface,str(score), im, c)

        # The Event Queue!
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:    #https://www.pygame.org/docs/ref/key.html
                if event.key == K_r:
                    score += 10

                elif event.key == K_UP:
                    score += 1
                elif event.key == K_DOWN:
                    score -= 1
                elif event.key == K_RIGHT:
                    c.move(5)
                elif event.key == K_LEFT:
                    c.move(-5)
                elif event.key == K_t:
                    pygame.mixer.Sound.play(my_sound)
            elif event.type == MOUSEBUTTONDOWN:
                (x, y) = (event.pos[0], event.pos[1])

                if hit(x,y,c):
                    c.new_color()

    pygame.quit()

main()
