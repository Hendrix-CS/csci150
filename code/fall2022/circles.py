import math

import pygame
from pygame.locals import *

import random

class Circle:
    def __init__(self, xmax, ymax):
        self.t = 0

        self.radius = 50
        self.x = random.randint(self.radius, xmax - self.radius)
        self.y = random.randint(self.radius, ymax - self.radius)

        # x velocity, i.e. amount x is changing each time step
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)

        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.color = pygame.Color(r,g,b)

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
        self.t += 0.05

        self.radius = 50 + math.sin(self.t) * 15

        if self.x - self.radius <= 0:
            self.vx = abs(self.vx)
        if self.x + self.radius >= xmax:
            self.vx = -abs(self.vx)
        if self.y - self.radius <= 0:
            self.vy = abs(self.vy)
        if self.y + self.radius >= ymax:
            self.vy = -abs(self.vy)

        self.x += self.vx
        self.y += self.vy

def draw_all(surface, circle_list):
    surface.fill(pygame.Color(255,255,255))

    for circle in circle_list:
        circle.draw(surface)

    pygame.display.update()

def main():
    pygame.init()
    xmax = 640
    ymax = 480
    surface = pygame.display.set_mode((xmax, ymax))

    circle_list = []

    running = True
    while running:
        pygame.time.wait(30)
        for circle in circle_list:
            circle.update(xmax, ymax)
        draw_all(surface, circle_list)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_c:
                circle_list.append(Circle(xmax, ymax))
            elif event.type == MOUSEBUTTONDOWN:
                (x, y) = event.pos
                for circle in circle_list:
                    if circle.contains(x, y):
                        circle.change_color()

    pygame.quit()

main()

