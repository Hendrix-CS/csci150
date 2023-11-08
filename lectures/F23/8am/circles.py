import pygame
from pygame.locals import *     # Some useful constants

import random

def random_color() -> Color:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return pygame.Color(r, g, b)

class Circle:

    def __init__(self, x: int, y: int, radius):
        self.x = x
        self.y = y

        self.vx = random.randint(-7, 7)
        self.vy = random.randint(-7, 7)

        self.radius = radius

        self.color = random_color()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def update(self, xmax, ymax):
        self.y += self.vy
        self.x += self.vx

        if self.y >= ymax - self.radius:
            self.vy *= -1
            self.color = random_color()
            self.vx = random.randint(-7, 7)
        if self.y <= self.radius:
            self.vy *= -1
            self.color = random_color()
            self.vx = random.randint(-7, 7)
        if self.x <= self.radius:
            self.vx *= -1
            self.color = random_color()
        if self.x >= xmax - self.radius:
            self.vx *= -1
            self.color = random_color()

def main():
    pygame.init()
    xmax = 640
    ymax = 480
    surface = pygame.display.set_mode((xmax, ymax))

    running = True

    circles: list[Circle] = []

    for i in range(50):
        r = random.randint(10, 75)
        x = random.randint(r, xmax-r)
        y = random.randint(r, ymax-r)
        circles.append(Circle(x,y,r))

    while running:
        pygame.time.wait(30)
        update_all(circles, xmax, ymax)
        draw_all(surface, circles)     # this is the function which does the drawing
        for event in pygame.event.get():   # this looks at the event queue to see if anything has happened.
            if event.type == QUIT:         # 'QUIT' is what happens when the user closes the window
                running = False

    pygame.quit()

def update_all(circles: list[Circle], xmax, ymax):
    for circle in circles:
        circle.update(xmax, ymax)

def draw_all(surface, circles: list[Circle]):
    surface.fill(pygame.Color(255, 255, 255))
    for circle in circles:
        circle.draw(surface)
    pygame.display.update()  # update the window once we're ready


main()
