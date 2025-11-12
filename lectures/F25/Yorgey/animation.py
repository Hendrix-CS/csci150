import pygame
from pygame.locals import *     # Some useful constants
from dataclasses import dataclass
import random

@dataclass
class Circle:
    x: int
    y: int
    vx: int       # x velocity, i.e. change in x coordinate in pixels per frame
    vy: int       # y velocity
    radius: int
    color: pygame.Color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def reverse(self):
        self.vx *= -1
        self.vy *= -1

    def update(self):
        if self.y + self.radius >= 480:
            self.vy = -abs(self.vy)
            # self.radius += 10
        if self.x + self.radius >= 640:
            self.vx = -abs(self.vx)
            # self.radius += 10
        if self.y - self.radius <= 0:
            self.vy = abs(self.vy)
            # self.radius += 10
        if self.x - self.radius <= 0:
            self.vx = abs(self.vx)
            # self.radius += 10

        self.x += self.vx
        self.y += self.vy

def main():
    pygame.init()    # this sets up the ability to draw to a window
    surface = pygame.display.set_mode( (640, 480) )
    clock = pygame.time.Clock()

    circles = []
    circles.append(Circle(100, 101, 3, 5, 50, pygame.Color(40, 100, 40)))
    circles.append(Circle(300, 400, -4, -2, 20, pygame.Color(22, 5, 255)))
    for i in range(100):
        x = random.randint(50, 590)
        y = random.randint(50, 430)
        r = random.randint(5, 50)
        c = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        vx = random.randint(-7, 7)
        vy = random.randint(-7, 7)
        circles.append(Circle(x, y, vx, vy, r, c))

    running = True
    while running:
        for circle in circles:
            circle.update()
        draw_all(surface, circles)     # this is the function which does the drawing
        for event in pygame.event.get():   # this looks at the event queue to see if anything has happened.
            if event.type == QUIT:         # 'QUIT' is what happens when the user closes the window
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    for circle in circles:
                        circle.reverse()

        clock.tick(40)

    pygame.quit()


def draw_all(surface, circles):
    surface.fill('white')

    for circle in circles:
        circle.draw(surface)

    pygame.display.update()  # update the window once we're ready

main()
