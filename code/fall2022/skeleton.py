import pygame
from pygame.locals import *

def draw_all(surface):
    surface.fill(pygame.Color(255,255,255))
    pygame.display.update()

def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 480))

    running = True
    while running:
        draw_all(surface)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    pygame.quit()

main()

