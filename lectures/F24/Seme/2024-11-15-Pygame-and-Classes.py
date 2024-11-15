from typing import *

import pygame
from pygame.locals import *
import random

## We go through my dumb "video game" today

# This builds the main character
class Character():

    def __init__(self):
        self.x = 400
        self.y = 200
        self.dir = + 1  # + 1 is right, -1 is left
        self.up = -40
        self.down = 220
        self.left = -50
        self.right = 50

    def draw(self, surface):
        # For the eye, nose, and foot, we pay attention to direction!

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
        self.radius = random.randint(10,50)
        self.explode = False
        self.timer = 0



        self.velx = random.randint(-3,3)
        self.vely = random.randint(-3,3)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self):
        if self.explode:
            self.velx = 0
            self.vely = 0
            self.radius += 5
            self.timer += 1 # this keeps track of how many frans so far it has exploded!
            self.color = 'yellow'
            if self.timer > 5:
                self.x = 10000
                self.y = 10000

        self.x += self.velx
        self.y += self.vely

    def exploded(self, hit_sound):
        if not self.explode:
            pygame.mixer.Sound.play(hit_sound)
        self.explode = True





####### The above are classes and their methods

def collide(t: 'Target', c: 'Character') -> bool:
    upper_left = (c.x+c.left, c.y+c.up)
    lower_right = (c.x+c.right,c.y + c.down)

    x = max(upper_left[0],min(t.x,lower_right[0]))
    y = max(upper_left[1],min(t.y,lower_right[1]))

    dx = x - t.x
    dy = y - t.y

    return dx ** 2 + dy ** y <= t.radius ** 2




def draw_all(surface, char_list, target_list, text_info,homer_image):
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

    # this puts the imge file on the screen
    surface.blit(homer_image,(850,100))

    pygame.display.update()



def hit(x, y, targ: Target):
    if (x - targ.x) ** 2 + (y - targ.y) ** 2 <= targ.radius ** 2:
        return True
    else:
        return False



# this is how I format the text that will be printed as the score
def set_text(string, coordx, coordy, fontSize): # Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize)
    # (0, 0, 0) is black, to make black text
    text = font.render(string, True, (255,255,255))
    textRect = text.get_rect()  # this figures out how large of a rectange the text needs
    textRect.center = (coordx, coordy)
    return (text, textRect)




def main2():
    pygame.init()

    pygame.mixer.init()
    hit_sound = pygame.mixer.Sound("doh.mp3") # loads the sound file
    surface = pygame.display.set_mode((1000, 800))
    reg_homer = pygame.image.load('homer1.png') #loads an image file
    reg_homer = pygame.transform.scale(reg_homer, (64, 64))  # resizes it to be 64 pixels by 64
    doh_homer = pygame.image.load('homer2.png')
    doh_homer = pygame.transform.scale(doh_homer, (64, 64))



    homer_image = reg_homer  # i use this to keep track of which homer image to show
    score = 0

    running = True
    char_list = []
    target_list = []
    me = Character()
    char_list.append(me)
    while running:
        draw_all(surface, char_list, target_list, str(score),homer_image)
        homer_image=reg_homer
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
                    if hit(x,y,targ) and not targ.explode:
                        targ.color = 'blue'
                        score += 1






        pygame.time.delay(30)

        # this loop runs through each target (i.e. circles) and
        # checks to see if they have hit the character
        for item in target_list:
            if collide(item, me):
                item.exploded(hit_sound)
                homer_image=doh_homer
            item.move()




    pygame.quit()

main2()





## Finally, a simple point and click keyboard

# class Key:
#
#     def __init__(self, x, y, letter):
#         self.x = x
#         self.y = y
#         self.letter = letter.upper()
#
#         self.size = 50
#         self.color = 'gray'
#
#     def draw(self, surface):
#         pygame.draw.rect(surface, self.color, (self.x, self.y, self.size,self.size))
#
#
#         totalText = set_text(self.letter, self.x + self.size // 2, self.y + self.size // 2 + 3, 30)
#         surface.blit(totalText[0], totalText[1])
#
#     def toggle_click(self):
#         if self.color == 'gray':
#             self.color = 'yellow'
#         else:
#             self.color = 'gray'
#
#
#
#
# def draw_all(surface, key_list: List['Key'], let):
#     surface.fill(pygame.Color('white'))
#
#     for key in key_list:
#         key.draw(surface)
#
#     totalText = set_text1(let, 100, 500, 30)
#     surface.blit(totalText[0], totalText[1])
#
#
#     pygame.display.update()
#
#
#
#
# def set_text(string, coordx, coordy, fontSize):
#     font = pygame.font.SysFont('Helvetica', fontSize)
#     # font.bold = True
#     text = font.render(string, True, (255,255,255))
#     textRect = text.get_rect()
#     textRect.center = (coordx, coordy)
#     return (text, textRect)
#
# def set_text1(string, coordx, coordy, fontSize):
#     font = pygame.font.SysFont('Helvetica', fontSize)
#     # font.bold = True
#     text = font.render(string, True, 'black')
#     textRect = text.get_rect()
#     textRect.center = (coordx, coordy)
#     return (text, textRect)
#
# def make_keys():
#     initx = 100
#     inity = 100
#     key_list = [['a','b','c'],['d','e','f'],['g','h','i']]
#     keys = []
#     deltax = 5
#     deltay = 5
#
#     currx = initx
#     curry = inity
#
#     for row in key_list:
#         for item in row:
#             keys.append(Key(currx, curry, item))
#             currx += deltax + 50
#         currx = initx
#         curry += deltay + 50
#
#     return keys
#
#
# def hit(x,y, key):
#     if key.x <= x <= key.x + key.size and key.y <= y <= key.y + key.size:
#         key.toggle_click()
#         if key.color == 'yellow':
#             return key.letter
#         else:
#             return None
#
#
# def main3():
#     pygame.init()
#     xmax = 1000
#     ymax = 800
#     surface = pygame.display.set_mode((xmax, ymax))
#
#     key_list = make_keys()
#     running = True
#
#     str = ''
#
#
#     while running:
#         draw_all(surface, key_list, str)
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
#                 for key in key_list:
#                     let = hit(x, y, key)
#
#                     if let:
#                         str += let
#
#
#
#
#
#
#
#
#
#         pygame.time.delay(30)
#
#
#
#     pygame.quit()
#
# #main3()