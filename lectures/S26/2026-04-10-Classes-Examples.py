# Quiz Today -- Dictionaries
# Homework Due Monday -- Classes
# Final Project Design Document -- Due Next Friday
#   * If working with partner, please *both* should turn in a copy
#   * If you are electing to not to a Final Project
#          please turn in a short document saying so


# We talked a bit about classes and the water jug lab
# I then showed an example where a group made their final project
# based on that lab

# I then introduced PyGame

import pygame
from pygame.locals import *

def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))
    surface.fill(pygame.Color(255, 255, 255))
    running = True
    while running:
        pygame.display.update()
        pygame.draw.circle(surface,'red',(50,50),23)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    pygame.quit()
