import pygame
from pygame.locals import *

import random

## We are going to do a graphical a key pad

class Key:

    def __init__(self,num: int, left: int, top: int):
        self.num = num
        self.left = left
        self.top = top
        self.size = 50

        self.color = 'black'
        self.text_color = 'white'


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.left, self.top, self.size,self.size))

        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render(str(self.num), True, self.text_color)
        textRect = text.get_rect()
        textRect.center = (self.left + self.size/2, self.top + self.size/2)

        surface.blit(text, textRect)

    def get_value(self) -> int:
        return self.num




def set_text(string, coordx, coordy, fontSize): # Function to set text
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text = font.render(string, True, (0,255,255))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)

def key_builder():
    startx = 100
    starty = 100
    deltax = 60
    deltay = 60

    currx = startx
    curry = starty

    key_list = []
    i = 1
    while i <= 9:
        key_list.append(Key(i, currx,curry))

        if i % 3 == 0:
            currx = startx
            curry += deltay
        else:
            currx += deltax

        i += 1

    return key_list


def draw_all(surface, key_list, str_so_far):
    surface.fill('white') # 'blank' the screen with basic background each time

    # Draw some shapes
    for item in key_list:
        item.draw(surface)

    totalText = set_text(str_so_far, 350, 30, 30)
    surface.blit(totalText[0], totalText[1])


    # This needs to be the final line of draw_all -- and only should appear *ONCE*
    pygame.display.update()

def hit(x :int, y: int, k: Key) -> bool:
    if k.left < x < k.left+k.size and k.top < y < k.top + k.size:
        return True
    else:
        return False


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))
    surface.fill(pygame.Color(255, 255, 255))

    key_list = key_builder()


    str_so_far = ''



    running = True
    while running:
        draw_all(surface,key_list, str_so_far)

        # The Event Queue!
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:    #https://www.pygame.org/docs/ref/key.html
                if event.key == K_x:
                    str_so_far = str_so_far[0:len(str_so_far) - 1]


            elif event.type == MOUSEBUTTONDOWN:
                (x,y) = (event.pos[0], event.pos[1])
                for k in key_list:
                    if hit(x,y,k):
                        str_so_far += str(k.get_value())



    pygame.quit()

main()