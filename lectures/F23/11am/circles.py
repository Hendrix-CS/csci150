import random

import pygame
from pygame.locals import *     # Some useful constants

def random_color() -> Color:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return pygame.Color(r,g,b)

class Circle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

        self.radius = 50

        self.color = random_color()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def update(self, xmax, ymax):
        bounced = False
        if self.y <= self.radius:
            self.vy = abs(self.vy)
            bounced = True
        if self.y >= ymax - self.radius:
            self.vy = -abs(self.vy)
            bounced = True
        if self.x <= self.radius:
            self.vx = abs(self.vx)
            bounced = True
        if self.x >= xmax - self.radius:
            self.vx = -abs(self.vx)
            bounced = True

        if bounced:
            self.vx *= 2
            self.vy *= 2
            self.color = random_color()

        self.x += self.vx
        self.y += self.vy

        # Change the velocity slightly
        self.vx += random.random()/5 - 1/10
        self.vy += random.random()/5 - 1/10

def main():
    pygame.init()
    xmax = 640
    ymax = 480
    surface = pygame.display.set_mode((xmax, ymax))
    running = True

    circles: list[Circle] = []

    for i in range(10):
        x = random.randint(0,640)
        y = random.randint(0,480)
        circles.append(Circle(x, y))

    while running:
        pygame.time.wait(30)
        update_all(circles, xmax, ymax)
        draw_all(surface, circles)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

    pygame.quit()


def draw_all(surface, circles):
    surface.fill(pygame.Color(255, 255, 255))

    for circle in circles:
        circle.draw(surface)

    pygame.display.update()  # update the window once we're ready


def update_all(circles, xmax, ymax):
    for circle in circles:
        circle.update(xmax, ymax)

main()
