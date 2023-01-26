from typing import *

import pygame
from pygame.locals import *
import random

# The last homework is assigned today (Classes and Dictionaries)
#  it is due on Wednesday

# We will officially assign project #3 on Monday.

# Exam #3 is coming up:
    # In-class Monday, November 21
    # Take Home: you will get the take-home at the end of class on Friday, Noveber 18
    #   due 11:59pm, Tuesday, Nov 22 (since Thanksgiving)


# What about complicated shapes?
# What about text?

class Character():

    def __init__(self):
        self.x = 400
        self.y = 200
        self.dir = + 1  # + 1 is right, -1 is left

    def draw(self, surface):
        # head
        pygame.draw.circle(surface, pygame.Color(220, 220, 220), (self.x,self.y), 40)

        # eye
        pygame.draw.circle(surface, 'yellow', (self.x + self.dir * 15, self.y), 10)

        # nose
        pygame.draw.polygon(surface, pygame.Color(220, 220, 220),[(self.x + self.dir*35,self.y-10),(self.x+self.dir*35,self.y+10),(self.x+self.dir*50,self.y+10)])

        # torso
        pygame.draw.rect(surface, pygame.Color(220, 220, 220),(self.x-50, self.y+40,100,100))

        # leg
        pygame.draw.rect(surface, pygame.Color(220, 220, 220), (self.x - 10, self.y + 140, 20, 80))

        # foot
        if self.dir == 1:
            pygame.draw.rect(surface, pygame.Color(220, 220, 220), (self.x - 10, self.y + 220, 40, 10))
        else:
            pygame.draw.rect(surface, pygame.Color(220, 220, 220), (self.x - 30, self.y + 220, 40, 10))


    def move(self, dir: int):
        if dir == self.dir:
            self.x += 3 * self.dir
        else:
            self.dir *= -1


class Target:

    def __init__(self):
        self.x = random.randint(0,1000)
        self.y = random.randint(0,800)
        self.color = 'red'

        self.velx = random.randint(-3,3)
        self.vely = random.randint(-3,3)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), 10)

    def move(self):
        self.x += self.velx
        self.y += self.vely






def draw_all(surface, char_list, target_list, text_info):
    surface.fill('black') # or whatever you background color is -- this 'refreshes' the screen

    for item in char_list:
        item.draw(surface)  # each thing in object list should be part of a class
        # and should have it own draw method

    for item in target_list:
        item.draw(surface)  # each thing in object list should be part of a class
        # and should have it own draw method

    # the below will add text (if you also have a set_text function)
    totalText = set_text(text_info, 100 , 50, 30) # what to print,
    surface.blit(totalText[0], totalText[1])

    pygame.display.update()



def hit(x, y, targ: Target):
    if (x - targ.x) ** 2 + (y - targ.y) ** 2 <= 100:
        return True
    else:
        return False



# this is how I format the text that will be printed as the score
def set_text(string, coordx, coordy, fontSize): # Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize)
    # (0, 0, 0) is black, to make black text
    text = font.render(string, True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)




def main1():
    pygame.init()
    surface = pygame.display.set_mode((1000, 800))

    score = 0
    running = True
    char_list = []
    target_list = []
    me = Character()
    char_list.append(me)
    while running:
        draw_all(surface, char_list, target_list, str(score))
        for event in pygame.event.get():
            if event.type == QUIT:
               running = False
            elif event.type == KEYDOWN:
                if event.key ==K_SPACE:
                    score += 5
                elif event.key == K_LEFT:
                    me.move(-1)
                elif event.key == K_RIGHT:
                    me.move(1)
                elif event.key == K_t:
                    target_list.append(Target())

            elif event.type == MOUSEBUTTONDOWN:
                (x,y) = (event.pos[0], event.pos[1])

                for targ in target_list:
                    if hit(x,y,targ):
                        targ.color = 'blue'
                        score += 1



        pygame.time.delay(30)
        for item in target_list:
            item.move()



    pygame.quit()

main1()

#
# # This just shows a more complicated version of what we did on Wednesday -- take in collisions!
# #
# class Circle():
#
#     def __init__(self):
#         self.x = random.randint(0,1000)
#         self.y = random.randint(0,800)
#
#         self.rad = random.randint(5,35)
#         self.color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#
#         self.velx = random.randint(-5,5)
#         self.vely = random.randint(-5,5)
#
#
#
#     def draw(self, surface):
#         pygame.draw.circle(surface,self.color, (self.x, self.y),self.rad)
#
#     def move(self, xmax, ymax):
#         if self.x < self.rad or self.x > xmax - self.rad: # has hit the left side of the screen!
#             self.velx *= -1
#
#         if self.y < self.rad or self.y > ymax - self.rad: # has hit the left side of the screen!
#             self.vely *= -1
#
#         self.x += self.velx
#         self.y += self.vely
#
#
#
#
#
#
# def draw_all(surface, circle_list):
#     surface.fill('white')
#
#     for circ in circle_list:
#         circ.draw(surface)
#
#     pygame.display.update()
#
#
# def hit(x, y, targ: Circle):
#     if (x - targ.x) ** 2 + (y - targ.y) ** 2 <= targ.rad ** 2:
#         return True
#     else:
#         return False
#
# def dist(c1: Circle, c2: Circle) -> bool:
#     return ((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2) ** (1 / 2) <= c1.rad + c2.rad
#
#
# # the below function is complicated -- it does the conversation of momentum for an elastic collision
# # This is beyond the scope of what I expect you to do in class, but does show how "real" word physics
# # can be used -- I am assuming that the mass of the objects is proportional to their area.
# def elastic(c1: Circle, c2: Circle):
#
#     v1 = (c1.velx, c1.vely)
#     x1 = (c1.x, c1.y)
#     m1 = c1.rad ** 2
#
#     v2 = (c2.velx, c2.vely)
#     x2 = (c2.x, c2.y)
#     m2 = c2.rad ** 2
#
#
#     new_v1x = v1[0] - (2 * m2)/(m1 + m2) * ((v1[0]-v2[0]) * (x1[0]-x2[0]) + (v1[1]-v2[1])*(x1[1]-x2[1]))/((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2) * (x1[0]-x2[0])
#
#     new_v1y = v1[1] - (2 * m2) / (m1 + m2) * ((v1[0] - v2[0]) * (x1[0] - x2[0]) + (v1[1] - v2[1]) * (x1[1] - x2[1])) / (
#                 (x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2) * (x1[1]-x2[1])
#
#     new_v2x = v2[0] - (2 * m1) / (m1 + m2) * ((v2[0] - v1[0]) * (x2[0] - x1[0]) + (v2[1] - v1[1]) * (x2[1] - x1[1])) / (
#                 (x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2) * (x2[0]-x1[0])
#     new_v2y = v2[1] - (2 * m1) / (m1 + m2) * ((v2[0] - v1[0]) * (x2[0] - x1[0]) + (v2[1] - v1[1]) * (x2[1] - x1[1])) / (
#             (x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2) * (x2[1]-x1[1])
#
#     c1.velx = new_v1x
#     c1.vely = new_v1y
#
#     c2.velx = new_v2x
#     c2.vely = new_v2y
#
#
#
#
#
#
#
# def main1():
#     pygame.init()
#     xmax = 1000
#     ymax = 800
#     surface = pygame.display.set_mode((xmax, ymax))
#
#     # these are two circles I added for testing purposes
#     # a = Circle()
#     # b = Circle()
#     # a.x = 100
#     # a.y = 400
#     # b.x = 900
#     # b.y = 400
#     #
#     # a.rad = 10
#     # b.rad = 10
#     #
#     # a.velx = 3
#     # b.velx = -3
#     # a.vely = 0
#     # b.vely = 0
#
#
#
#     circle_list = []
#     # circle_list.append(a) # again, for test purposes
#     # circle_list.append(b)
#     running = True
#
#     while running:
#         draw_all(surface, circle_list)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                running = False
#             elif event.type == KEYDOWN:
#                 if event.key ==K_c:
#                     circle_list.append(Circle())
#
#
#             elif event.type == MOUSEBUTTONDOWN:
#                 (x,y) = (event.pos[0], event.pos[1])
#
#                 for circ in circle_list:
#                     if hit(x,y,circ):
#                         circ.color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#
#
#
#
#         pygame.time.delay(30)
#         for item in circle_list:
#             item.move(xmax, ymax)
#
#         for i in range(len(circle_list)):
#             for j in range(i+1, len(circle_list)):
#                 if dist(circle_list[i], circle_list[j]):
#
#                     elastic(circle_list[i], circle_list[j]) # this does the elastic collision (mostly)
#
#                     # # these make the circles bounce off each other, but in awkward ways
#                     # circle_list[i].velx *= -1
#                     # circle_list[j].velx *= -1
#                     # circle_list[i].vely *= -1
#                     # circle_list[j].vely *= -1
#
#
#
#
#
#
#     pygame.quit()
#
# main1()





