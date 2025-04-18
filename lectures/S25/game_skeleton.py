import math
import random
import pygame
from pygame.locals import *

# A Game object will store all the data about the
# current state of the game.
class Game:

    def __init__(self):

        # Objects list will hold all the objects in the game,
        # which must all have .update() and .draw() methods.
        self.objects = []

    def update(self, surface):
        for o in self.objects:
            o.update(surface)

    def draw(self, surface):
        surface.fill('white')

        for o in self.objects:
            o.draw(surface)

        pygame.display.update()

# handle_input handles all user input, and returns True
# if the game should keep running, False if it should quit.
def handle_input(game: Game) -> bool:
    for event in pygame.event.get():
        if event.type == QUIT:
            return False

    return True

def main():
    pygame.init()
    surface = pygame.display.set_mode((640*2, 480*2))

    game = Game()

    clock = pygame.time.Clock()

    running = True
    while running:
        game.update(surface)
        game.draw(surface)
        running = handle_input(game)
        clock.tick(40)

    pygame.quit()

main()
