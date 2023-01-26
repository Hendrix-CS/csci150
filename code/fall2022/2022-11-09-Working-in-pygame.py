from typing import *
import pygame
from pygame.locals import * # this lets you have more control

import random


# General Outline: -- main

# pygame.init()
# surface = pygame.display.set_mode((xwidth, ywidth))

# running = True
# while running:
#     draw current frame -- usually a function on its own!
#     check for events (keyboard, mouse, etc)
#     update state




# Let's write some code that will, each time I hit the 'c' button
# on the keyboard, put a circle, with random location and random
# color on the screen

# notice that we will need a list to contain the circles

# def circle_build():
#     # we want to create a circle, with random center, color
#     # how can we keep up with that?
#
#     r_color = random.randint(0,255)
#     b_color = random.randint(0,255)
#     g_color = random.randint(0,255)
#
#     x_center = random.randint(20,620) # not too close to either edge
#     y_center = random.randint(20, 460)  # not too close to either edge
#
#     # now we want to return all of this!!
#     color = (r_color,b_color,g_color)
#     center = (x_center,y_center)
#
#     return (color,center)
#
# def draw_all(surface,circle_list):
#     surface.fill(pygame.Color(255, 255, 255))  # what color to use to fill out the background
#
#     for i in range(len(circle_list)):
#         pygame.draw.circle(surface, pygame.Color(circle_list[i][0]), circle_list[i][1], 20)
#
#     pygame.display.update()
#
#
# def main1():
#     pygame.init()
#     surface = pygame.display.set_mode((640, 480))
#
#     circle_list = []
#
#
#     # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
#     running = True
#     while running:
#         draw_all(surface,circle_list) # this is the function which does the drawing
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 running = False
#             elif event.type == KEYDOWN:
#                 if event.key == K_c:
#                     circle_list.append(circle_build())
#
#     pygame.quit()
#
# main1()
#
#
# #######
# # Okay, but what if I wanted to have them move? Or if I click on them, they change color?
# #
# #We use a class!
# #


##########################
# This exactly replicates the above code, but with a circle class
# class Circle:
#
#     def __init__(self):
#         self.r_color = random.randint(0, 255)
#         self.b_color = random.randint(0, 255)
#         self.g_color = random.randint(0, 255)
#
#         self.x_center = random.randint(20, 620)  # not too close to either edge
#         self.y_center = random.randint(20, 460)  # not too close to either edge
#
#
#
#
# def draw_all(surface,circle_list):
#     surface.fill(pygame.Color(255, 255, 255))  # what color to use to fill out the background
#
#     for circ in circle_list:
#         pygame.draw.circle(surface, pygame.Color(circ.r_color,circ.b_color,circ.g_color), (circ.x_center,circ.y_center), 20)
#
#     pygame.display.update()
#
#
# def main1():
#     pygame.init()
#     surface = pygame.display.set_mode((640, 480))
#
#     circle_list = []
#
#
#     # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
#     running = True
#     while running:
#         draw_all(surface,circle_list) # this is the function which does the drawing
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 running = False
#             elif event.type == KEYDOWN:
#                 if event.key == K_c:
#                     circle_list.append(Circle())
#
#     pygame.quit()
#
# main1()




########################
# Now, we expand -- we want to add two abilities
# If we click on a circle, it will change to a new color
# We want the circle to move in a random direction --  and to "bounce" off of the edges!

# I am going to once again copy the code from above....

# class Circle:
#
#     def __init__(self):
#         self.r_color = random.randint(0, 255)
#         self.b_color = random.randint(0, 255)
#         self.g_color = random.randint(0, 255)
#
#         self.x_center = random.randint(20, 600)  # not too close to either edge
#         self.y_center = random.randint(20, 420)  # not too close to either edge
#
#         self.radius = random.randint(5,30)
#
#         self.x_vel = random.randint(1,5) * (-1) ** random.randint(0,1)
#         self.y_vel = random.randint(1, 5) * (-1) ** random.randint(0, 1)
#
#     def color_change(self):
#         self.r_color = random.randint(0, 255)
#         self.b_color = random.randint(0, 255)
#         self.g_color = random.randint(0, 255)
#
#     def move(self,xmax,ymax):
#         if self.x_center - self.radius <= 0:
#             self.x_vel *= -1
#         if self.x_center + self.radius >= xmax:
#             self.x_vel *= -1
#
#         if self.y_center - self.radius <= 0:
#             self.y_vel *= -1
#         if self.y_center + self.radius >= ymax:
#             self.y_vel *= -1
#
#         self.x_center += self.x_vel
#         self.y_center += self.y_vel
#
#
#
#
# def hit(x, y, targ: Circle): # to determine if the mouse clicked on it
#     if (x - targ.x_center) ** 2 + (y - targ.y_center) ** 2 <= targ.radius ** 2: #pythagorean theorem/distance formula
#         return True
#     else:
#         return False
#
# def draw_all(surface,circle_list):
#     surface.fill(pygame.Color(255, 255, 255))  # what color to use to fill out the background
#
#     for circ in circle_list:
#         pygame.draw.circle(surface, pygame.Color(circ.r_color,circ.b_color,circ.g_color), (circ.x_center,circ.y_center), circ.radius)
#
#     pygame.display.update()
#
#
# def main1():
#     xmax = 640
#     ymax = 480
#     pygame.init()
#     surface = pygame.display.set_mode((xmax, ymax))
#
#     circle_list = []
#
#
#     # the while loop below will keep the screen 'active' until you quit (i.e. click the close box)
#     running = True
#     while running:
#         draw_all(surface,circle_list) # this is the function which does the drawing
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 running = False
#             elif event.type == KEYDOWN:
#                 if event.key == K_c:
#                     circle_list.append(Circle())
#
#             elif event.type == MOUSEBUTTONDOWN:
#                 (x,y) = (event.pos[0], event.pos[1])
#
#                 for circ in circle_list:
#                     if hit(x,y,circ):
#                         circ.color_change()
#
#         pygame.time.delay(30)
#         for item in circle_list:
#             item.move(xmax, ymax)
#
#     pygame.quit()
#
# main1()






#
#
#
#
#
# # Putting objects in the screen -- last time, but reminder
#
# # Using a class!
#
# class Character():
#
#     def __init__(self):
#         self.x = 400
#         self.y = 200
#         self.dir = + 1  # + 1 is right, -1 is left
#
#     def draw(self, surface):
#         # head
#         pygame.draw.circle(surface, pygame.Color(220, 220, 220), (self.x,self.y), 40)
#
#         # eye
#         pygame.draw.circle(surface, 'yellow', (self.x + self.dir * 15, self.y), 10)
#
#         # nose
#         pygame.draw.polygon(surface, pygame.Color(220, 220, 220),[(self.x + self.dir*35,self.y-10),(self.x+self.dir*35,self.y+10),(self.x+self.dir*50,self.y+10)])
#
#         # torso
#         pygame.draw.rect(surface, pygame.Color(220, 220, 220),(self.x-50, self.y+40,100,100))
#
#         # leg
#         pygame.draw.rect(surface, pygame.Color(220, 220, 220), (self.x - 10, self.y + 140, 20, 80))
#
#         # foot
#         if self.dir == 1:
#             pygame.draw.rect(surface, pygame.Color(220, 220, 220), (self.x - 10, self.y + 220, 40, 10))
#         else:
#             pygame.draw.rect(surface, pygame.Color(220, 220, 220), (self.x - 30, self.y + 220, 40, 10))
#
#
#     def move(self, dir: int):
#         if dir == self.dir:
#             self.x += 3 * self.dir
#         else:
#             self.dir *= -1
#
#
# class Target:
#
#     def __init__(self):
#         self.x = random.randint(0,1000)
#         self.y = random.randint(0,800)
#         self.color = 'red'
#
#         self.velx = random.randint(-3,3)
#         self.vely = random.randint(-3,3)
#
#     def draw(self, surface):
#         pygame.draw.circle(surface, self.color, (self.x, self.y), 10)
#
#     def move(self):
#         self.x += self.velx
#         self.y += self.vely
#
#
#
#
#
# # Mouse Inputs
#
# # Printing Text to the Screen
#
# def draw_all(surface, char_list, target_list, text_info, offset):
#     surface.fill('black') # or whatever you background color is -- this 'refreshes' the screen
#
#     for item in char_list:
#         item.draw(surface)  # each thing in object list should be part of a class
#         # and should have it own draw method
#
#     for item in target_list:
#         item.draw(surface)  # each thing in object list should be part of a class
#         # and should have it own draw method
#
#     # the below will add text (if you also have a set_text function)
#     totalText = set_text(text_info, 100 + offset, 50, 30) # what to print,
#     surface.blit(totalText[0], totalText[1])
#
#     pygame.display.update()
#
#
#
# def hit(x, y, targ: Target):
#     if (x - targ.x) ** 2 + (y - targ.y) ** 2 <= 100:
#         return True
#     else:
#         return False
#
#
#
# # this is how I format the text that will be printed as the score
# def set_text(string, coordx, coordy, fontSize): # Function to set text
#
#     font = pygame.font.Font('freesansbold.ttf', fontSize)
#     # (0, 0, 0) is black, to make black text
#     text = font.render(string, True, (255,255,255))
#     textRect = text.get_rect()
#     textRect.center = (coordx, coordy)
#     return (text, textRect)
#
#
#
#
# def main1():
#     pygame.init()
#     surface = pygame.display.set_mode((1000, 800))
#
#     score = 0
#     offset = 0
#     running = True
#     char_list = []
#     target_list = []
#     me = Character()
#     char_list.append(me)
#     while running:
#         draw_all(surface, char_list, target_list, str(score), offset)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                running = False
#             elif event.type == KEYDOWN:
#                 if event.key ==K_SPACE:
#                     score += 5
#                 elif event.key == K_LEFT:
#                     me.move(-1)
#                 elif event.key == K_RIGHT:
#                     me.move(1)
#                 elif event.key == K_t:
#                     target_list.append(Target())
#                 elif event.key == K_s:
#                     offset += 5
#             elif event.type == MOUSEBUTTONDOWN:
#                 (x,y) = (event.pos[0], event.pos[1])
#
#                 for targ in target_list:
#                     if hit(x,y,targ):
#                         targ.color = 'blue'
#                         score += 1
#
#
#
#         pygame.time.delay(30)
#         for item in target_list:
#             item.move()
#
#
#
#     pygame.quit()
#
# main1()

# But this is awkward. We can make some improvement, but for the next project, if you want something like this, let me know

