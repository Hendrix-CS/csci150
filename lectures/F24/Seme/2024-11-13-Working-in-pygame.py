from typing import *
import pygame
from pygame.locals import * # this lets you have more control

import random



# The Design Document is due Friday
# See my sample, linked on the class calendar




# General Outline:

# pygame.init()
# surface = pygame.display.set_mode((xwidth, ywidth))

# running = True
# while running:
#     draw current frame -- using a draw_all() function ,or similar
#     check for events (keyboard, mouse, etc)
#     update state


# draw_all() -- which might take in multiple parameters:
#  draws a complete refresh of the screen as needed:

#
    # surface.fill('black') # or whatever you background color is -- this 'refreshes' the screen
    #
    # then, for each object (hey, that word might be useful!) that goes on the screen,
    # you need to draw it
    #
    # pygame.display.update() -- this should be the last line in your draw_all() function
    #    and should be called *exactly* once in the entire program!!!

# If one or more objects on the screen are 100% static, maybe we can draw them from a list or something
# Otherwise, (and maybe even with static things) a CLASS is the thing to do

# Each object (a character's avatar, enemies, moving background objects, etc
# will be its own object -- and will know its position on the screen
# we will then have a draw() method for each class


## Let's start simple -- we are going to make some circles and rectangle
# They will have random locations and colors
# When you click on a circle, it will change to black

# class Circle:
#
#     def __init__(self):
#         self.x = random.randint(200,800)
#         self.y = random.randint(200,600)
#         self.radius = 30
#
#         self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#
#
#
#     def draw(self, surface):
#         pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
#
#
#
#
# class Rectangle:
#
#     def __init__(self):
#         self.x = random.randint(200, 800)
#         self.y = random.randint(200, 600)
#         self.width = random.randint(10, 50)
#         self.height = random.randint(10, 50)
#
#         self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#
#
#     def draw(self, surface):
#         pygame.draw.rect(surface,self.color,(self.x, self.y, self.width, self.height))
#
#
#
# def hit(x, y, target):
#     if isinstance(target, Circle):
#         if (x - target.x) ** 2 + (y - target.y) ** 2 <= target.radius ** 2:
#             target.color = 'black'
#
# def draw_all(surface, shape_list):
#     surface.fill('white')
#
#     for item in shape_list:
#         item.draw(surface)
#
#
#
#
#     pygame.display.update()
#
#
# def main():
#     pygame.init()
#     surface = pygame.display.set_mode((1000, 800))
#
#
#     running = True
#     shape_list = []
#     while running:
#         draw_all(surface, shape_list)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                running = False
#             elif event.type == KEYDOWN:
#                 if event.key ==K_c:
#                     shape_list.append(Circle())
#                 elif event.key == K_r:
#                     shape_list.append(Rectangle())
#
#
#
#             elif event.type == MOUSEBUTTONDOWN:
#                 (x,y) = (event.pos[0], event.pos[1])
#                 for item in shape_list:
#                     hit(x, y, item)
#
#         pygame.time.delay(30)
#
#
#
#
#
#
#
#
#     pygame.quit()
#
# main()





# class Circle:
#
#     def __init__(self):
#         self.x = random.randint(200,800)
#         self.y = random.randint(200,600)
#         self.radius = random.randint(10,50)
#
#         self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#
#         self.velx = ((-1) ** random.randint(0,1)) * random.randint(1,5)
#         self.vely = ((-1) ** random.randint(0, 1)) * random.randint(1, 5)
#
#     def draw(self, surface):
#         pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
#
#     def move(self):
#         self.x += self.velx
#         self.y += self.vely
#
#
#
#
# class Rectangle:
#
#     def __init__(self):
#         self.x = random.randint(200, 800)
#         self.y = random.randint(200, 600)
#         self.width = random.randint(10, 50)
#         self.height = random.randint(10, 50)
#
#         self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#
#         self.velx = ((-1) ** random.randint(0, 1)) * random.randint(1, 5)
#         self.vely = ((-1) ** random.randint(0, 1)) * random.randint(1, 5)
#
#     def draw(self, surface):
#         pygame.draw.rect(surface,self.color,(self.x, self.y, self.width, self.height))
#
#     def move(self):
#         self.x += self.velx
#         self.y += self.vely
#
#
#
# def draw_all(surface, shape_list):
#     surface.fill('white')
#
#     for item in shape_list:
#         item.draw(surface)
#
#
#
#
#     pygame.display.update()
#
#
# def main():
#     pygame.init()
#     surface = pygame.display.set_mode((1000, 800))
#
#
#     running = True
#     shape_list = []
#     while running:
#         draw_all(surface, shape_list)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                running = False
#             elif event.type == KEYDOWN:
#                 if event.key ==K_c:
#                     shape_list.append(Circle())
#                 elif event.key == K_r:
#                     shape_list.append(Rectangle())
#
#
#
#
#
#         pygame.time.delay(30)
#         for item in shape_list:
#             item.move()
#
#
#
#
#
#
#
#     pygame.quit()
#
# main()
############################################




###################################################################
###################################################################
# Example 2


# When one of the moving circles hits the character, it 'explodes' and a sound is played:
# We also make the targets start out with random radi
#
# class Character():
#
#     def __init__(self):
#         self.x = 400
#         self.y = 200
#         self.dir = + 1  # + 1 is right, -1 is left
#         self.up = -40
#         self.down = 220
#         self.left = -50
#         self.right = 50
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
#         self.radius = random.randint(10,50)
#         self.explode = False
#         self.timer = 0
#
#
#
#         self.velx = random.randint(-3,3)
#         self.vely = random.randint(-3,3)
#
#     def draw(self, surface):
#         pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
#
#     def move(self):
#         if self.explode:
#             self.velx = 0
#             self.vely = 0
#             self.radius += 5
#             self.timer += 1
#             self.color = 'yellow'
#             if self.timer > 5:
#                 self.x = 10000
#                 self.y = 10000
#
#         self.x += self.velx
#         self.y += self.vely
#
#     def exploded(self, hit_sound):
#         if not self.explode:
#             pygame.mixer.Sound.play(hit_sound)
#         self.explode = True
#
#
#
#
#
# ####### The above are classes and their methods
#
# def collide(t: 'Target', c: 'Character') -> bool:
#     upper_left = (c.x+c.left, c.y+c.up)
#     lower_right = (c.x+c.right,c.y + c.down)
#
#     x = max(upper_left[0],min(t.x,lower_right[0]))
#     y = max(upper_left[1],min(t.y,lower_right[1]))
#
#     dx = x - t.x
#     dy = y - t.y
#
#     return dx ** 2 + dy ** y <= t.radius ** 2
#
#
#
#
# def draw_all(surface, char_list, target_list, text_info, offset):
#     surface.fill('black') # or whatever you background color is -- this 'refreshes' the screen
#
#     for item in char_list:
#         item.draw(surface)  # each thing in object list should be part of a class
#         # and should have it own draw method
#
#     # pygame.draw.circle(surface,'green',(-1,643),35)
#     # pygame.draw.circle(surface, 'orange', (-20, -10), 105)
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
#     if (x - targ.x) ** 2 + (y - targ.y) ** 2 <= targ.radius ** 2:
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
# def main2():
#     pygame.init()
#
#     pygame.mixer.init()  # this lets you have access to playing sounds
#     hit_sound = pygame.mixer.Sound("doh.mp3")
#     surface = pygame.display.set_mode((1000, 800))
#
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
#                     if hit(x,y,targ) and not targ.explode:
#                         targ.color = 'blue'
#                         score += 1
#
#
#
#
#
#
#         pygame.time.delay(30)
#         for item in target_list:
#             if collide(item, me):
#                 item.exploded(hit_sound)
#             item.move()
#
#
#
#
#     pygame.quit()
#
# main2()

