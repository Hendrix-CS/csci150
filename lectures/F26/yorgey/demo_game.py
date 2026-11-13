import math
import random
import pygame
from pygame.locals import *
from dataclasses import dataclass

MOVE_AMOUNT = 20
MOVE_CHANCE = 0.15

@dataclass
class Racer:
    x: float
    y: float
    color: pygame.Color

    def update(self, surface):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), 20)

    def won(self, surface) -> bool:
        return self.x >= surface.get_width() - 100

    def move(self):
        self.x += MOVE_AMOUNT

# A Game object will store all the data about the
# current state of the game.
class Game:

    def __init__(self, surface):

        self.surface = surface

        # Objects list will hold all the objects in the game,
        # which must all have .update() and .draw() methods.
        self.objects = []
        self.computers = []

        self.player = Racer(100, 100, pygame.Color('blue'))
        self.objects.append(self.player)

        for i in range(8):
            computer = Racer(100, 200 + 100*i, pygame.Color('pink'))
            self.computers.append(computer)
            self.objects.append(computer)

        self.screen = 'game'

    def update(self):
        if self.screen != 'game':
            return

        for o in self.objects:
            o.update(self.surface)

        if self.player.won(self.surface):
            print("You win!")
            self.screen = 'win'
        elif self.computer_won():
            print("You lose =(")
            self.screen = 'lose'

        for computer in self.computers:
            if random.random() < MOVE_CHANCE:
                computer.move()

    def draw(self):
        self.surface.fill('white')

        for o in self.objects:
            o.draw(self.surface)

        if self.screen == 'win':
            pygame.draw.circle(self. surface, 'green', (320, 400), 100)

        pygame.display.update()

    def computer_won(self) -> bool:
        for computer in self.computers:
            if computer.won(self.surface):
                return True
        return False

# handle_input handles all user input, and returns True
# if the game should keep running, False if it should quit.
def handle_input(game: Game) -> bool:
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                game.player.move()

    return True

def main():
    pygame.init()
    surface = pygame.display.set_mode((640*2, 480*2))

    game = Game(surface)

    clock = pygame.time.Clock()

    running = True
    while running:
        game.update()
        game.draw()
        running = handle_input(game)
        clock.tick(40)

    pygame.quit()

main()
