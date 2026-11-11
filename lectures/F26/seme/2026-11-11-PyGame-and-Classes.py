# Reminders
# * Final Project Design Document Due Next Monday
# * Quiz #10 Friday (Classes)

# * There us *NOT* a quiz for this week's material (just lab)



from dataclasses import dataclass
import pygame
from pygame.locals import *
import random




# this is the 'bare bones' code that will allow us to
# start up PyGame and have a surface
#
# We are going to:
#
# -- Add circles to the screen when the 't' key is pressed
# --  when built, a circle will appear at a random location
# --  and random velocities

# we will then talk about other things we can add

def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))

    running = True

    while running:



        # The Event Queue!
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False



main()