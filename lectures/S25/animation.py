import pygame
from pygame.locals import *     # Some useful constants
from dataclasses import dataclass
import random

@dataclass
class Circle:
    x: int
    y: int
    vx: int    # x velocity
    vy: int    # y velocity
    radius: int
    color: pygame.Color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # check if the circle is hitting the bottom edge
        if (480 - self.y) <= self.radius:
            self.vy *= -1
        if (640 - self.x) <= self.radius:
            self.vx *= -1
        if self.y <= self.radius:
            self.vy *= -1
        if self.x <= self.radius:
            self.vx *= -1

def main():
    pygame.init()    # this sets up the ability to draw to a window
    surface = pygame.display.set_mode( (640, 480) )
    # 'surface' is the name of the window
    # where we will draw. We set its size to 640 x 480 pixels.

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True

    circles = []
    circles.append(Circle(200, 300, 5, 7, 50, pygame.Color('blue')))
    circles.append(Circle(100, 200, -3, 4, 70, pygame.Color('red')))
    for i in range(20):
        x = random.randint(50, 590)
        y = random.randint(50, 430)
        color = pygame.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255), 100)
        rad = random.randint(10, 50)
        vx = random.randint(-10, 10)
        vy = random.randint(-10, 10)
        circles.append(Circle(x, y, vx, vy, rad, color))
    clock = pygame.time.Clock()

    while running:
        clock.tick(30)
        update_all(circles)
        draw_all(surface, circles)     # this is the function which does the drawing
        for event in pygame.event.get():   # this looks at the event queue to see if anything has happened.
            if event.type == QUIT:         # 'QUIT' is what happens when the user closes the window
                running = False

    pygame.quit()

def update_all(circles):
    for circle in circles:
        circle.update()

def draw_all(surface, circles):
    surface.fill('white')

    for circle in circles:
        circle.draw(surface)

    pygame.display.update()  # update the window once we're ready

main()
