from typing import *
import pygame
from pygame.locals import * # this lets you have more control

import random

# Reminders
# Exam #3 is next Monday -- practice Exam and solutions are posted
# Homework #9 (the *last* homework) is due on Wednesday
#
# Project #3 is Assigned
# You need to turn in a design document by next Monday -- details on Project #3 page


# General Outline:

# pygame.init()
# surface = pygame.display.set_mode((xwidth, ywidth))

# running = True
# while running:
#     draw current frame
#     check for events (keyboard, mouse, etc)
#     update state








# Putting objects in the screen -- last imte, but reminder
# Directly
# Using a class!

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





# Mouse Inputs

# Printing Text to the Screen

def draw_all(surface, char_list, target_list, text_info):
    surface.fill('black') # or whatever you background color is -- this 'refreshes' the screen

    for item in char_list:
        item.draw(surface)  # each thing in object list should be part of a class
        # and should have it own draw method

    for item in target_list:
        item.draw(surface)  # each thing in object list should be part of a class
        # and should have it own draw method

    # the below will add text (if you also have a set_text function)
    totalText = set_text(text_info, 100, 50, 30) # what to print,
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

# But this is awkward. We can make some improvement, but for the next project, if you want something like this, let me know

