import pygame
from pygame.locals import *

import random




class Circle:

    def __init__(self):
        self.x = random.randint(0,640)
        self.y = random.randint(0,400)
        self.radius = random.randint(5,25)
        self.color = 'red'

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)




def draw_all(surface, circle_list):
    surface.fill('white') # 'blank' the screen with basic background each time

    # Draw some shapes
    for item in circle_list:
        item.draw(surface)


    # This needs to be the final line of draw_all -- and only should appear *ONCE*
    pygame.display.update()


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))
    surface.fill(pygame.Color(255, 255, 255))

    circle_list = []

    running = True
    while running:
        draw_all(surface,circle_list)

        # The Event Queue!
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:    #https://www.pygame.org/docs/ref/key.html
                if event.key == K_c:
                    circle_list.append(Circle())

            elif event.type == MOUSEBUTTONDOWN:
                (x,y) = (event.pos[0], event.pos[1])


    pygame.quit()

main()