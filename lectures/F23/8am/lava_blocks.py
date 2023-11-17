import math
import random

import pygame
from pygame.locals import *

# Where can we look for help adding text to PyGame?
#
# - PyGame documentation
# - Ask a friend
# - Google it!   "how to add text to the screen in PyGame"
#   - Or search YouTube
# - Ask ChatGPT or GitHub Copilot ...

SECOND_EVENT = pygame.USEREVENT + 1

class Score:

    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 64)

    def add(self, s: int):
        self.score += s

    def reset(self):
        self.score = 0

    def update(self, surface):
        pass

    def draw(self, surface):
        # Referred to https://www.geeksforgeeks.org/python-display-text-to-pygame-window/#
        # for an example of how to draw text

        text = self.font.render(str(self.score), True, 'black')
        textRect = text.get_rect()
        textRect.center = (40, 40)

        surface.blit(text, textRect)

class Lava:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vx = random.randint(-7, 7)
        self.vy = random.randint(-7, 7)

    def draw(self, surface):
        pygame.draw.rect(surface, 'red', self.hitbox())

    def update(self, surface):
        self.x += self.vx
        self.y += self.vy

    def hitbox(self) -> Rect:
        return Rect((self.x, self.y), (50, 50))

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

        self.image = pygame.transform.scale(pygame.image.load("pygame.png"), (50, 50))

    def draw(self, surface):
        imgRect = self.image.get_rect()
        imgRect.center = (self.x, self.y)
        surface.blit(self.image, imgRect)
        # pygame.draw.polygon(surface, 'green', [(self.x - 20, self.y), (self.x + 20, self.y), (self.x, self.y - 20 * math.sqrt(3))])

    def update(self, surface):
        self.x += self.vx
        self.y += self.vy

    def add_vel(self, vx, vy):
        self.vx += vx
        self.vy += vy

    def hitbox(self) -> Rect:
        return Rect((self.x - 15, self.y - 30), (30, 30))

# A Game object will store all the data about the
# current state of the game
class Game:

    def __init__(self):
        self.player = Player(200, 200)

        # Objects list will hold all the objects in the game,
        # which must all have .update() and .draw() methods.
        self.objects = []
        self.objects.append(self.player)

        self.lava_blocks = []

        self.score = Score()
        self.objects.append(self.score)

    def update(self, surface):
        if random.random() < 0.3:
            lava = Lava(random.randint(0, surface.get_width()), random.randint(0, surface.get_height()))
            self.lava_blocks.append(lava)
            self.objects.append(lava)

        for o in self.objects:
            o.update(surface)

        for lava in self.lava_blocks:
            if self.player.hitbox().colliderect(lava.hitbox()):
                print("Ouch!")
                self.score.reset()

    def draw(self, surface):
        surface.fill('white')

        for o in self.objects:
            o.draw(surface)

        # pygame.draw.rect(surface, 'blue', self.player.hitbox())

        pygame.display.update()

def handle_input(game: Game) -> bool:
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                game.player.add_vel(0,5)
            elif event.key == K_UP:
                game.player.add_vel(0, -5)
            elif event.key == K_RIGHT:
                game.player.add_vel(5, 0)
            elif event.key == K_LEFT:
                game.player.add_vel(-5, 0)
        elif event.type == KEYUP:
            if event.key == K_DOWN:
                game.player.add_vel(0, -5)
            elif event.key == K_UP:
                game.player.add_vel(0, 5)
            elif event.key == K_RIGHT:
                game.player.add_vel(-5, 0)
            elif event.key == K_LEFT:
                game.player.add_vel(5, 0)

        elif event.type == SECOND_EVENT:
            game.score.add(1)

    return True

def main():
    pygame.init()
    surface = pygame.display.set_mode((640*2, 480*2))

    game = Game()

    pygame.time.set_timer(SECOND_EVENT, 1000)

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(40)
        game.update(surface)
        game.draw(surface)
        running = handle_input(game)

    pygame.quit()

main()