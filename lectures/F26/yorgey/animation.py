import pygame
import random
from pygame.locals import *     # Some useful constants
from dataclasses import dataclass

@dataclass
class Circle:
    x: float
    y: float
    vx: float   # x velocity, i.e. how much x changes per frame
    vy: float   # y velocity
    color: pygame.Color
    radius: int

    # Every Circle object knows how to update itself each frame
    def update(self):
        if self.y + self.radius >= 480:
            self.vy *= -1
        if self.y - self.radius <= 0:
            self.vy *= -1
        if self.x + self.radius >= 640:
            self.vx *= -1
        if self.x - self.radius <= 0:
            self.vx *= -1

        self.x += self.vx
        self.y += self.vy

    # Every Circle object knows how to draw itself
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def attract(self, goal: tuple[int,int]):
        dx = goal[0] - self.x
        dy = goal[1] - self.y

        self.vx += dx/1000
        self.vy += dy/1000

def main():
    pygame.init()    # this sets up the ability to draw to a window
    surface = pygame.display.set_mode( (640, 480) )
    # 'surface' is the name of the window
    # where we will draw. We set its size to 640 x 480 pixels.

    circles = []
    for i in range(10):
        x = random.randint(50, 590)
        y = random.randint(50, 430)
        r = random.randint(10, 50)
        vx = random.randint(-5, 5)
        vy = random.randint(-5, 5)
        color = pygame.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        circles.append(Circle(x, y, vx, vy, color, r))

    clock = pygame.time.Clock()

    # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
    running = True

    while running:
        for event in pygame.event.get():   # this looks at the event queue to see if anything has happened.
            if event.type == QUIT:         # 'QUIT' is what happens when the user closes the window
                running = False

            elif event.type == MOUSEMOTION:
                mouse_pos = event.pos

                for circle in circles:
                    circle.attract(mouse_pos)

        for circle in circles:
            circle.update()
        draw_all(surface, circles)     # this is the function which does the drawing

        clock.tick(40)  # Set FPS to 40

    pygame.quit()


def draw_all(surface, circles):
    surface.fill('white')

    for circle in circles:
        circle.draw(surface)

    pygame.display.update()  # update the window once we're ready

main()
