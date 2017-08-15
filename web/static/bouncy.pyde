# Can you read me

import random

XMAX = 1280
YMAX = 960

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return add(self, other)
    
    def __sub__(self, other):
        return sub(self, other)
    
    def scale(self,k):
        return Vector(self.x * k, self.y * k)
    
    def length(self):
        return (self.x ** 2 + self.y ** 2)**(1/2)
    
    def normalize(self):
        return self.scale(1/self.length())
    
def add(v1, v2):
    return Vector(v1.x + v2.x, v1.y + v2.y)

def sub(v1, v2):
    return Vector(v1.x - v2.x, v1.y - v2.y)

class Ball:
    def __init__(self, pos, r, vel):
        self.pos = pos
        self.r = r
        self.vel = vel
        
        self.colors = ['0x08ffe5', '0x0adbf6', '0x157382', '0x105219']
        self.curcolor = 0
    
    def update(self):
        if self.pos.x - self.r <= 0:
            self.vel.x *= -1
            self.change_color()
        if self.pos.x + self.r >= XMAX:
            self.vel.x *= -1
            self.change_color()
        if self.pos.y - self.r <= 0:
            self.vel.y *= -1
            self.change_color()
        if self.pos.y + self.r >= YMAX:
            self.vel.y *= -1
            self.change_color()
        
        self.pos += self.vel

    def change_color(self):        
        self.curcolor += 1
        self.curcolor %= len(self.colors)
    
    def draw(self):
        fill(self.colors[self.curcolor])
        ellipse(self.pos.x, self.pos.y, 2*self.r, 2*self.r)

class World:
    def __init__(self):
        self.balls = []
    
    def add_ball(self, ball):
        self.balls.append(ball)
        
    def update(self):
        for b in self.balls:
            b.update()
    
    def draw(self):
        # background('0xffffff')
        for b in self.balls:
            b.draw()

world = World()

def setup():
    size(XMAX, YMAX)
    for i in range(10):
        r = random.randint(30, 150)
        x = random.randint(r, XMAX - r)
        y = random.randint(r, YMAX - r)
        vx = random.randint(-10, 10)
        vy = random.randint(-10, 10)
        world.add_ball(Ball(Vector(x,y), r, Vector(vx, vy)))

def draw():
    world.update()
    world.draw()