import math
import random
from dataclasses import dataclass
import pygame
from pygame.locals import *

@dataclass
class Player:
    x: int
    y: int

    vx: int
    vy: int

    def draw(self, surface):
        pygame.draw.rect(surface, 'blue', (self.x - 20, self.y - 20, 40, 40))

        # pygame.draw.rect(surface, 'green', self.hitbox(), width=3)

    def update(self, surface):
        self.x += self.vx
        self.y += self.vy

    def adjust_vx(self, d):
        self.vx += d

    def hitbox(self) -> pygame.Rect:
        return Rect(self.x - 20, self.y - 20, 40, 40)

@dataclass
class Enemy:
    x: int
    y: int
    vx: int
    vy: int
    radius: int
    off_bottom: bool = False

    def draw(self, surface):
        pygame.draw.circle(surface, 'red', (self.x, self.y), self.radius)

        # pygame.draw.rect(surface, 'green', self.hitbox(), width=3)

    def update(self, surface):
        self.x += self.vx
        self.y += self.vy

    def hitbox(self) -> pygame.Rect:
        return Rect(self.x - self.radius, self.y - self.radius, 2*self.radius, 2*self.radius)

# A Game object will store all the data about the
# current state of the game.
class Game:

    def __init__(self, surface):

        self.surface = surface

        self.lose = False

        # Objects list will hold all the objects in the game,
        # which must all have .update() and .draw() methods.
        self.objects = []

        self.player = Player(self.surface.get_width() / 2, self.surface.get_height() - 100, 0, 0)
        self.objects.append(self.player)

        self.player_speed = 8

        self.enemies = []
        self.score = 0

    def update(self):
        r = random.random()
        if r < (1/5):
            r = random.randint(20, 100)
            x = random.randint(r, self.surface.get_width() - r)
            vy = random.randint(5, 12)
            enemy = Enemy(x, r + 20, 0, vy, r)
            self.enemies.append(enemy)
            self.objects.append(enemy)

        for o in self.objects:
            o.update(self.surface)

        for enemy in self.enemies:
            if enemy.hitbox().colliderect(self.player.hitbox()):
                self.lose = True
            elif enemy.y - enemy.radius > self.surface.get_height() and not enemy.off_bottom:
                enemy.off_bottom = True
                self.score += 1
                print(self.score)

    def draw(self):
        self.surface.fill('white')

        for o in self.objects:
            o.draw(self.surface)

        pygame.display.update()

# handle_input handles all user input, and returns True
# if the game should keep running, False if it should quit.
def handle_input(game: Game) -> bool:
    for event in pygame.event.get():
        if event.type == QUIT:
            return False

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                game.player.adjust_vx(game.player_speed)
            elif event.key == K_LEFT:
                game.player.adjust_vx(-game.player_speed)
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                game.player.adjust_vx(-game.player_speed)
            elif event.key == K_LEFT:
                game.player.adjust_vx(game.player_speed)

    return True

def main():
    pygame.init()
    surface = pygame.display.set_mode((640*2, 480*2))

    game = Game(surface)

    clock = pygame.time.Clock()

    running = True
    while running and not game.lose:
        game.update()
        game.draw()
        running = handle_input(game)
        clock.tick(40)

    pygame.quit()

main()
