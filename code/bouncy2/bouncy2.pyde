import random
import math

XMAX = 640
YMAX = 480

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def copy(self):
        return Vector(self.x, self.y)

    def scale(self, k):
        self.x *= k
        self.y *= k
        
        return self
    
    def scaled(self, k):
        return Vector(self.x * k, self.y * k)

    def normalize(self):
        l = self.length()
        self.scale(1/l)

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return sub(self, other)

def add(v1,v2):
    return Vector(v1.x + v2.x, v1.y + v2.y)

def sub(v1,v2):
    return Vector(v1.x - v2.x, v1.y - v2.y)

def dist(p1, p2):
    return sub(p2,p1).length()

def dot(v1, v2):
    return v1.x*v2.x + v1.y*v2.y

class Ball:
    def __init__(self, c, r, v):
        self.c = c
        self.r = r
        self.v = v

    def draw(self):
        ellipse(self.c.x, self.c.y, 2*self.r, 2*self.r)

    def intersect(self, other):
        return dist(self.c, other.c) <= (self.r + other.r)

    def update(self):
        if self.c.x + self.r >= XMAX or self.c.x - self.r <= 0:
            self.v.x *= -1
        if self.c.y + self.r >= YMAX or self.c.y - self.r <= 0:
            self.v.y *= -1
        
        self.c += self.v

    def bounce(self, other):
        if (self.intersect(other)):
            # normal = self.c - other.c
            # normal.normalize()
            
            # aci = dot(self.v, normal)
            # bci = dot(other.v, normal)
            
            m1 = self.r**2
            m2 = other.r**2
            # acf = (aci * (m1 - m2) + 2 * m2 * bci) / (m1 + m2)
            # bcf = (bci * (m2 - m1) + 2 * m1 * aci) / (m1 + m2)
            
            u1 = self.v.copy()
            u2 = other.v.copy()
            
            self.v = (u1.scaled(m1 - m2) + u2.scaled(2*m2)).scaled(1/(m1 + m2))
            other.v = (u2.scaled(m2 - m1) + u1.scaled(2*m1)).scaled(1/(m1 + m2))
            
            # normal.scale(acf - aci)
            # self.v += normal
            
            # normal.scale(2*dot(normal, self.v))
            # self.v = self.v - normal

class World:
    def __init__(self, n):
        self.balls = []
        while len(self.balls) < n:
            r = random.randint(10, 100)
            x = random.randint(r, XMAX-r)
            y = random.randint(r, YMAX-r)
            vx = 2 * random.random() - 1
            vy = 2 * random.random() - 1
            new_ball = Ball(Vector(x,y),r, Vector(vx, vy))

            ok = True
            for ball in self.balls:
                if (ball.intersect(new_ball)):
                    ok = False
            if ok:
                self.balls.append(new_ball)

    def draw(self):
        background('#FFFFFF')
        for ball in self.balls:
            ball.draw()

    def update(self):
        for i in range(len(self.balls) - 1):
            for j in range(i+1, len(self.balls)):
                bi = self.balls[i]
                bj = self.balls[j]
                bi.bounce(bj)
                # bj.bounce(bi)

        for ball in self.balls:
            ball.update()

world = World(10)

def draw():
    world.update()
    world.draw()

def setup():
    size(XMAX, YMAX)