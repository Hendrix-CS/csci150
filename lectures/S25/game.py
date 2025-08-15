import math
import random
import pygame
from pygame.locals import *
from dataclasses import dataclass

@dataclass
class Enemy:
    x: int
    y: int

    vx: int = 0
    vy: int = 7

    def update(self, surface):
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        pygame.draw.polygon(surface, 'red', [(self.x - 10, self.y + 10), (self.x + 10, self.y + 10), (self.x, self.y - 10)])
        # pygame.draw.rect(surface, 'blue', self.hitbox())

    def hitbox(self) -> Rect:
        return Rect((self.x - 10, self.y - 10), (20, 20))

@dataclass
class Player:
    x: int
    y: int

    vx: int = 0
    vy: int = 0

    radius: int = 50

    def add_vel(self, dx, dy):
        self.vx += dx
        self.vy += dy

    def update(self, surface):
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        pygame.draw.circle(surface, 'gray73', (self.x, self.y), self.radius)
        pygame.draw.circle(surface, 'greenyellow', (self.x - self.radius/2, self.y - self.radius/2), self.radius/3)
        pygame.draw.circle(surface, 'green2', (self.x + self.radius/2, self.y - self.radius/2), self.radius/3)

        # pygame.draw.rect(surface, 'blue', self.hitbox())

    def hitbox(self):
        return Rect((self.x - self.radius*0.8, self.y - self.radius*0.8), (1.6*self.radius, 1.6*self.radius))

# A Game object will store all the data about the
# current state of the game.
class Game:

    def __init__(self):

        # Objects list will hold all the objects in the game,
        # which must all have .update() and .draw() methods.
        self.objects = []
        self.enemies = []

        self.player = Player(200, 200)

        self.objects.append(self.player)

        self.game_over = False

    def update(self, surface):
        if random.random() < 0.23:
            x = random.randint(0, surface.get_width())
            enemy = Enemy(x, 0)
            self.enemies.append(enemy)
            self.objects.append(enemy)

        for o in self.objects:
            o.update(surface)

        # Check whether player is touching any enemies
        for enemy in self.enemies:
            if enemy.hitbox().colliderect(self.player.hitbox()):
                self.game_over = True

    def draw(self, surface):
        surface.fill('white')

        if self.game_over:
            pygame.draw.circle(surface, 'red', (500, 500), 300)
        else:
            for o in self.objects:
                o.draw(surface)

        pygame.display.update()

# handle_input handles all user input, and returns True
# if the game should keep running, False if it should quit.
def handle_input(game: Game) -> bool:
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                game.player.add_vel(5, 0)
            elif event.key == K_LEFT:
                game.player.add_vel(-5, 0)
            elif event.key == K_UP:
                    game.player.add_vel(0, -5)
            elif event.key == K_DOWN:
                game.player.add_vel(0, 5)
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                game.player.add_vel(-5, 0)
            elif event.key == K_LEFT:
                game.player.add_vel(5, 0)
            elif event.key == K_UP:
                    game.player.add_vel(0, 5)
            elif event.key == K_DOWN:
                game.player.add_vel(0, -5)

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
