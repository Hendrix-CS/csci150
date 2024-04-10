import pygame
from pygame.locals import *


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))
    rects = []
    running = True
    while running:
        surface.fill(pygame.Color(255, 255, 255))
        for r in rects:
            pygame.draw.rect(surface, pygame.Color(255, 0, 0), (r[0], r[1], 40, 20))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                rects.append(event.pos)
    pygame.quit()


if __name__ == '__main__':
    main()