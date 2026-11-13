# Reminders
# * Final Project Design Document Due Next Monday
# * Quiz #10 Today (Classes)

# Class went a bit differently today.  Rather than writing the code,
# we played the game first and tried to understand what classes might
# be needed and what methods

# I will share the code at the end of class (on the class webpage, like always)



















from dataclasses import dataclass
import pygame
from pygame.locals import *
import random

@dataclass
class Player:

    y: int
    alive: bool


    def draw(self, surface):
        color = 'green'
        if not self.alive:
            color = 'gray'
        pygame.draw.polygon(surface,color,[(5,self.y-10),(20,self.y),(5,self.y+10)])

    def up(self):
        if self.alive:
            self.y -= 5

    def down(self):
        if self.alive:
            self.y += 5


@dataclass
class Enemy:

    x: int
    y: int
    rad: int

    def draw(self,surface):
        pygame.draw.circle(surface,'red',(self.x,self.y),self.rad)

    def move(self):
        self.x -= 5

    def destroy(self):
        self.x = -100


@dataclass
class Torpedo:

    x: int
    y: int

    def draw(self,surface):
        pygame.draw.circle(surface,'yellow',(self.x,self.y),2)

    def move(self):
        self.x += 5

    def destroy(self):
        self.x = 1000



def draw_all(surface, p, torp_list, enemy_list):
    surface.fill('black')

    p.draw(surface)

    for torp in torp_list:
        torp.draw(surface)

    for enemy in enemy_list:
        enemy.draw(surface)


    pygame.display.update()





def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))

    p = Player(200, True)
    torp_list = []
    enemy_list = []

    counter = 0

    when = random.randint(15,100) # when to spawn next enemy



    running = True

    while running:
        draw_all(surface, p, torp_list,enemy_list)

        # The Event Queue!
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if p.alive:
                        torp = Torpedo(21, p.y)
                        torp_list.append(torp)

                elif event.key == K_UP:
                    p.up()


                elif event.key == K_DOWN:
                    p.down()

        # Update State of Object!
        if p.alive:
            for torp in torp_list:
                torp.move()

            for enemy in enemy_list:
                enemy.move()

        # detect torpedo hitting enemy
        for torp in torp_list:
            for enemy in enemy_list:
                if (torp.x - enemy.x) ** 2 + (torp.y - enemy.y) ** 2 <= 25 ** 2:
                    torp.destroy()
                    enemy.destroy()

        for enemy in enemy_list:
            if (enemy.x - 20) ** 2 + (enemy.y - p.y) ** 2 <= 25 ** 2:
                p.alive = False

        #spawns enemies
        counter += 1
        if counter == when:
            when = random.randint(15,100)
            counter = 0
            enemy = Enemy(640, random.randint(0,400),25)
            enemy_list.append(enemy)


        pygame.time.delay(10)




main()