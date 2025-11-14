# We built, live in class, a simple version of the Google Dinosaur no internet game
# A wagon that jumps when you push the spacebar
# 'Cacti' (just rectangles) that randomly appear
#
# We did not have time to do collision detection or a score or anything.


import pygame
from pygame.locals import *
import random

from dataclasses import dataclass

@dataclass
class Wagon:
    x: int
    y: int
    vel: int = 0


    def draw(self,surface):
        # wheels
        pygame.draw.circle(surface,'brown',(self.x-10,self.y),10)
        pygame.draw.circle(surface, 'brown', (self.x - 50, self.y), 10)

        #body
        pygame.draw.polygon(surface,'brown',[(self.x-10,self.y),(self.x-50,self.y),(self.x-60,self.y-20),(self.x,self.y-20)])


    def jump(self):
        self.vel = -30

    def update(self):
        self.vel += 5
        self.y += self.vel
        if self.y >= 400:
            self.y = 400
            self.vel = 0
@dataclass
class Cactus:
    height: int
    x: int = 1000
    y: int = 410
    width: int = 10

    def draw(self,surface):
        pygame.draw.rect(surface,'black',(self.x,self.y-self.height,self.width, self.height))


    def update(self):
        self.x -= 10


def draw_all(surface, w, rect_list):
    surface.fill('white') # or whatever you background color is -- this 'refreshes' the screen

    w.draw(surface)

    for c in rect_list:
        c.draw(surface)



    pygame.display.update()




def main2():
    pygame.init()
    surface = pygame.display.set_mode((1000, 800))

    running = True
    w = Wagon(100,400)
    rect_list = []
    while running:
        draw_all(surface, w,rect_list)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key ==K_SPACE:
                    w.jump()

        if random.random() < 0.1:
            height = random.randint(5,15)
            rect_list.append(Cactus(height))

        for c in rect_list:
            c.update()
        w.update()



        pygame.time.delay(100)

    pygame.quit()

main2()

