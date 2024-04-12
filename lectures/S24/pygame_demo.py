import math

import pygame
from pygame.locals import *


class Shape:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def move(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def colliding_with(self, other):
        for point in other.perimeter_points():
            if self.contains(point):
                return True
        return False


class RedRectangle(Shape):
    def __init__(self, pos):
        super().__init__(pos)

    def draw(self, surface):
        pygame.draw.rect(surface, pygame.Color(255, 0, 0),
                         (self.x, self.y, 40, 20))

    def contains(self, point):
        return self.x <= point[0] <= self.x + 40 and self.y <= point[1] <= self.y + 20

    def perimeter_points(self):
        return [(self.x, self.y),
                (self.x + 40, self.y),
                (self.x, self.y + 20),
                (self.x + 40, self.y + 20)]


class BlueCircle(Shape):
    def __init__(self, pos):
        super().__init__(pos)

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color(0, 0, 255), (self.x, self.y), 30)

    def contains(self, point):
        distance = math.sqrt((point[0] - self.x) ** 2 + (point[1] - self.y) ** 2)
        return distance <= 30

    def perimeter_points(self):
        return [(self.x - 30, self.y),
                (self.x, self.y - 30),
                (self.x + 30, self.y),
                (self.x, self.y + 30)]


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))
    shapes = []
    running = True
    is_placing = True
    while running:
        surface.fill(pygame.Color(255, 255, 255))
        for r in shapes:
            r.draw(surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if is_placing:
                    is_placing = False
                    if len(shapes) % 2 == 1:
                        shapes.append(RedRectangle(event.pos))
                    else:
                        shapes.append(BlueCircle(event.pos))
                else:
                    is_placing = True
            elif event.type == MOUSEMOTION:
                if not is_placing and len(shapes) > 0:
                    shapes[-1].move(event.pos)
                    do_not_remove = []
                    for i in range(len(shapes) - 1):
                        if type(shapes[i]) == type(shapes[-1]) or not shapes[-1].colliding_with(shapes[i]):
                            do_not_remove.append(shapes[i])
                    do_not_remove.append(shapes[-1])
                    shapes = do_not_remove

    pygame.quit()


if __name__ == '__main__':
    main()
