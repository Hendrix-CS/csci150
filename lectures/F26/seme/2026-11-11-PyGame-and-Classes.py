# Reminders
# * Final Project Design Document Due Next Monday
# * Quiz #10 Friday (Classes)

# * There us *NOT* a quiz for this week's material (just lab)



from dataclasses import dataclass
import pygame
from pygame.locals import *
import random




# this is the 'bare bones' code that will allow us to
# start up PyGame and have a surface
#
# We are going to:
#
# -- Add circles to the screen when the 't' key is pressed
# --  when built, a circle will appear at a random location
# --  and random velocities

# we will then talk about other things we can add
@dataclass
class Circle:

    color: str
    x: int
    y: int
    radius: int
    velx: int
    vely: int


    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.velx
        self.y += self.vely

        # Asteriods version
        # if self.x <= 0:
        #     self.x = 640 + self.x
        #
        # if self.x >= 640:
        #     self.x = self.x - 640
        #
        # if self.y <= 0:
        #     self.y = 400 + self.y
        #
        # if self.y >= 400:
        #     self.y = self.y - 400


        # Bounding off the wall version
        if self.x <= 0:
            self.velx *= -1

        if self.x >= 640:
            self.velx *= -1

        if self.y <= 0:
            self.vely *= -1

        if self.y >= 400:
            self.vely *= -1





def draw_all(surface,circle_list):
    surface.fill('white')

    for c in circle_list:
        c.draw(surface)







    pygame.display.update()











def circle_builder():
    x = random.randint(0,640)
    y = random.randint(0,400)
    radius = random.randint(10,50)
    velx = random.randint(-5,5)
    vely = random.randint(-5,5)

    return Circle('red',x,y,radius,velx, vely)





def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))

    circle_list = []



    running = True

    while running:
        draw_all(surface, circle_list)

        # The Event Queue!
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:    #https://www.pygame.org/docs/ref/key.html
                if event.key == K_t:
                    c = circle_builder()
                    circle_list.append(c)

        # Update State of Object!
        for c in circle_list:
            c.move()

        pygame.time.delay(10)




main()