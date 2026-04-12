# Reminders
# * Final Project Design Document Due Friday
# * Quiz #10 Friday (Classes)
# * Homework (Classes) due today
# * There us *NOT* a quiz for this week's material (just lab)

# PyGame -- a library which allows you to:
# * Draw shapes on a window
# * Add in .jpeg and other images
# * Detect keyboard/mouse input
# * Play sound
#
# Office Documentation:
# * https://www.pygame.org/docs/
#
# For the Final Project:
# * You do not need to cite any code you use/modify from class/lab
# * You do not need to cite any assistance you get from
#     * Me
#     * Dr. Delavan or Dr. Yorgey
#     * Lab/Help Center TAs
# * Offical PyGame (or Python) documentation
# BUT MUST Cite anything else

# The PyGame Library
# Each time you make a new project that uses PyGamae, you'll need to:
# * Open the Terminal
#     - Click on the rectangle that looks like >_
# * type pip install pygame-ce
# Try is *NOW* -- if this does not work, let me know!

import pygame
from pygame.locals import *

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
#
# def draw_all(surface):
#     pygame.draw.circle(surface, 'red', (50, 50), 23)
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
# Full Example
############

# How to draw shapes
# How to put text onto the screen
# How to 'blit' images to the screen
# How to play sounds
# Keyboard input
# Mouse clicks (next time)

# Shapes:

# pygame.draw.circle(where, color, (centerx, centery), radius)
# pygame.draw.rect(where, color, (topleftx, toplefty, wdith, height))
# pygame.draw.line(where, color, (startx,starty),(endx,endy))

# Text:
# this is how I format the text that will be printed as the score
# def set_text(string, coordx, coordy, fontSize): # Function to set text
#     font = pygame.font.Font('freesansbold.ttf', fontSize)
#     text = font.render(string, True, (0,0,255))
#     textRect = text.get_rect()
#     textRect.center = (coordx, coordy)
#     return (text, textRect)
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
# def draw_all(surface, score, im):
#     surface.fill('white') # 'blank' the screen with basic background each time
#
#     # Draw some shapes
#     pygame.draw.circle(surface, 'red', (50, 50), 23)
#     pygame.draw.rect(surface, 'green', (300,200,50,100))
#
#
#     # Add some text
#     totalText = set_text(score, 350,30, 30)
#     surface.blit(totalText[0], totalText[1])
#
#     # Add an image:
#     surface.blit(im, (100,100))
#
#
#     # This needs to be the final line of draw_all -- and only should appear *ONCE*
#     pygame.display.update()
#
#
# def main():
#     pygame.init()
#     surface = pygame.display.set_mode((640, 400))
#     surface.fill(pygame.Color(255, 255, 255))
#
#     my_sound = pygame.mixer.Sound('tos_photon_torpedo.mp3')
#
#     score = 0
#     im = pygame.image.load('enterprise.jpg')
#
#     running = True
#     while running:
#         draw_all(surface,str(score), im)
#
#         # The Event Queue!
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 running = False
#             elif event.type == KEYDOWN:    #https://www.pygame.org/docs/ref/key.html
#                 if event.key == K_r:
#                     score += 10
#
#                 elif event.key == K_UP:
#                     score += 1
#                 elif event.key == K_DOWN:
#                     score -= 1
#                 elif event.key == K_t:
#                     pygame.mixer.Sound.play(my_sound)
#
#     pygame.quit()
#
# main()


