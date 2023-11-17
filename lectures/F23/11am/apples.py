import math
import random
import pygame
from pygame.locals import *

# Where could we look for information/help on displaying images in PyGame?
#
# - PyGame documentation ("Sprite"?)
# - Google ("how do I display images in PyGame?")
# - Other resources you have been given
# - ChatGPT/GitHub Copilot/etc. - ask them to write an example program

# Drawing text:
# https://stackoverflow.com/a/10077748/305559
# # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
# myfont = pygame.font.SysFont("monospace", 15)
#
# # render text
# label = myfont.render("Some text!", 1, (255,255,0))
# screen.blit(label, (100, 100))
#
# https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
class Score:
    def __init__(self):
        self.score = 0

        self.font = pygame.font.SysFont("monospace", 60)

    def update(self, surface):
        pass

    def draw(self, surface):
        txt = self.font.render(str(self.score), 1, 'black')
        surface.blit(txt, (100, 100))

    def should_delete(self):
        return False

class Apple:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.eaten = False

    def update(self, surface):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, 'red', (self.x, self.y), 8)

        # pygame.draw.rect(surface, 'blue', self.hitbox(), width=2)

    def should_delete(self) -> bool:
        return self.eaten

    def hitbox(self) -> Rect:
        return Rect(self.x - 8, self.y - 8, 16, 16)

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

        # Used https://www.geeksforgeeks.org/python-display-images-with-pygame/#
        # and https://pythonprogramming.net/displaying-images-pygame/
        # as examples for how to load + draw images

        self.image = pygame.image.load("pythonlogo.png")

    def update(self, surface):
        self.x += self.vx
        self.y += self.vy

    def draw_stick_figure(self, surface):
        pygame.draw.line(surface, 'black', (self.x, self.y-10), (self.x, self.y+10))
        pygame.draw.line(surface, 'black', (self.x, self.y+10), (self.x-10, self.y+20))
        pygame.draw.line(surface, 'black', (self.x, self.y+10), (self.x+10, self.y+20))
        pygame.draw.circle(surface, 'black', (self.x, self.y - 20), 10, width=1)
        pygame.draw.line(surface, 'black', (self.x-5,self.y), (self.x+5, self.y))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def hitbox(self) -> Rect:
        return Rect(self.x-10, self.y-30, 20, 50)

    def should_delete(self) -> bool:
        return False

# Go through a list and get rid of all the things for which .should_delete() is True.
# Return a new list containing only the non-deleted things.
def prune(items: list) -> list:
    new_items = []
    for item in items:
        if not item.should_delete():
            new_items.append(item)

    return new_items

# A Game object will store all the data about the
# current state of the game.
class Game:

    def __init__(self):

        self.num_apples = 0
        self.player = Player(300, 300)

        apple = Apple(100, 100)
        self.apples = [apple]

        self.score = Score()

        # Objects list will hold all the objects in the game,
        # which must all have .update() and .draw() methods.
        self.objects = [self.player, apple, self.score]

    def update(self, surface):
        for o in self.objects:
            o.update(surface)

        for apple in self.apples:
            if self.player.hitbox().colliderect(apple.hitbox()):
                self.num_apples += 1
                print(self.num_apples)
                apple.eaten = True
                self.spawn_apple(surface)
                self.score.score += 1

        if random.random() < 0.05:
            self.spawn_apple(surface)

        self.apples = prune(self.apples)
        self.objects = prune(self.objects)

    def spawn_apple(self, surface):
        new_apple = Apple(random.randint(0, surface.get_width()), random.randint(0, surface.get_height()))
        self.objects.append(new_apple)
        self.apples.append(new_apple)

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
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                game.player.vx += 5
            elif event.key == K_LEFT:
                game.player.vx -= 5
            elif event.key == K_DOWN:
                game.player.vy += 5
            elif event.key == K_UP:
                game.player.vy -= 5
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                game.player.vx -= 5
            elif event.key == K_LEFT:
                game.player.vx += 5
            elif event.key == K_DOWN:
                game.player.vy -= 5
            elif event.key == K_UP:
                game.player.vy += 5

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
