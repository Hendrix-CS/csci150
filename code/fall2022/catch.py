import math

import pygame
from pygame.locals import *

import random

class Circle:
    def __init__(self, xmax, ymax):

        self.radius = 50
        self.x = random.randint(self.radius, xmax - self.radius)
        self.y = -self.radius

        # x velocity, i.e. amount x is changing each time step
        self.vx = 0
        self.vy = 0

        self.ax = 0
        self.ay = 0.7   # gravity

        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.color = pygame.Color(r,g,b)

        self.deleted = False

    def contains(self, x, y):
        return (x - self.x)**2 + (y - self.y)**2 <= self.radius**2

    def change_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = pygame.Color(r, g, b)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def update(self, xmax, ymax):
        self.vx += self.ax
        self.vy += self.ay

        self.x += self.vx
        self.y += self.vy

    def intersects(self, rect):
        (x, y, w, h) = rect
        return self.x >= x and self.x <= (x + w) and (self.y + self.radius >= y) and (self.y - self.radius <= (y + h))

class Basket:
    def __init__(self, xmax, ymax):
        self.x = xmax/2
        self.y = ymax - 30

        self.moving = False
        self.vx = 0

        self.deleted = False

    def draw(self, surface):
        pygame.draw.rect(surface, pygame.Color('black'), (self.x, self.y, 100, 20))

    def update(self, xmax, ymax):
        if self.moving:
            self.x += self.vx

    def start_moving(self, v):
        self.moving = True
        self.vx = v

    def stop_moving(self):
        self.moving = False
        self.vx = 0

    def rect(self):
        return (self.x, self.y, 100, 20)

def draw_all(surface, circle_list):
    surface.fill(pygame.Color(255,255,255))

    for circle in circle_list:
        circle.draw(surface)

    pygame.display.update()

def remove_deleted(lst):
    new_lst = []
    for thing in lst:
        if not thing.deleted:
            new_lst.append(thing)
    return new_lst

def main():
    pygame.init()
    xmax = 640
    ymax = 480
    surface = pygame.display.set_mode((xmax, ymax))

    basket_speed = 15

    thing_list = []
    circle_list = []
    score = 0

    the_basket = Basket(xmax, ymax)
    thing_list.append(the_basket)

    running = True
    while running:
        pygame.time.wait(30)

        # Possibly spawn a circle
        r = random.random()
        if r < 0.02:    # 2% chance
            new_circle = Circle(xmax, ymax)
            thing_list.append(new_circle)
            circle_list.append(new_circle)

        for thing in thing_list:
            thing.update(xmax, ymax)
            if (thing.y > 2*ymax):
                thing.deleted = True

        # Check which circles have hit the basket
        for circle in circle_list:
            if circle.intersects(the_basket.rect()):
                score += 1
                print(f"Caught! Score = {score}")
                circle.deleted = True

        thing_list = remove_deleted(thing_list)
        circle_list = remove_deleted(circle_list)

        print(len(circle_list))
        draw_all(surface, thing_list)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    the_basket.start_moving(-basket_speed)
                elif event.key == K_RIGHT:
                    the_basket.start_moving(basket_speed)
            elif event.type == KEYUP:
                the_basket.stop_moving()

    pygame.quit()

main()

