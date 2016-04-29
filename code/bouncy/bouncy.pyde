import random
import math

XMAX = 640
YMAX = 480

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
    
    def length(self):
        return dist(self, Vector(0,0))
    
    def scale(self, k):
        self.x *= k
        self.y *= k
    
    def normalize(self):
        l = self.length()
        self.scale(1/l)

def add(v1, v2):
    return Vector(v1.x + v2.x, v1.y + v2.y)

def sub(v1, v2):
    return Vector(v1.x - v2.x, v1.y - v2.y)

def dist(v1, v2):
    return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)

def dot(v1, v2):
    return v1.x*v2.x + v1.y*v2.y

def perp(v):
    return Vector(v.y, -v.x)

class Thingy:
    def update(self):
        pass
    def draw(self):
        pass
    def bounce(self, other):
        pass
    def intersects(self, other):
        return False
   
class Ball(Thingy):
    def __init__(self, c, r, v):
        self.c = c
        self.r = r
        self.v = v
    
    def draw(self):
        ellipse(self.c.x,self.c.y,2*self.r,2*self.r)

    def intersects(self, other):
        if (isinstance(other, Ball)):
            return (dist(self.c, other.c) <= (self.r + other.r))
        elif (isinstance(other, Wall)):
            n = other.normal()
            d = abs(dot(n, sub(self.c, other.p1)))
            return d <= self.r
        else:
            return False 
        
    def update(self):
        self.c = add(self.c, self.v)
        
    def bounce(self, other):
        if self.intersects(other):
            if isinstance(other, Ball):
                normal = sub(self.c, other.c)
            else:
                normal = other.normal()
            normal.normalize()
            normal.scale(2*dot(self.v,normal))
            self.v = sub(self.v, normal)
            
class Wall(Thingy):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def draw(self):
        line(self.p1.x,self.p1.y,self.p2.x,self.p2.y)
 
    def normal(self):
        n = perp(sub(self.p2, self.p1))
        n.normalize()
        return n
    
    def intersects(self, other):
        if isinstance(other, Ball):
            return other.intersects(self)
        else:
            return False
                                                       
class World:
    def __init__(self, n):
        self.thingys = []
        while len(self.thingys) < n:
            if random.random() < 0.2:
                x1 = random.randint(0, XMAX)
                y1 = random.randint(0, YMAX)
                x2 = random.randint(0, XMAX)
                y2 = random.randint(0, YMAX)
                new_thing = Wall(Vector(x1,y1), Vector(x2,y2))
            else:
                r = 30
                x = random.randint(r, XMAX - r)
                y = random.randint(r, YMAX - r)
                vx = 2 * random.random() - 1
                vy = 2 * random.random() - 1

                new_thing = Ball(Vector(x,y), r, Vector(vx,vy))
            ok = True
            for thing in self.thingys:
                if thing.intersects(new_thing):
                    ok = False
            if ok:
                self.thingys.append(new_thing)
        ul = Vector(0,0)
        ur = Vector(XMAX,0)
        lr = Vector(XMAX, YMAX)
        ll = Vector(0, YMAX)
        self.thingys.append(Wall(ul,ur))
        self.thingys.append(Wall(ur,lr))
        self.thingys.append(Wall(lr,ll))
        self.thingys.append(Wall(ll,ul))
            
    def draw(self):
        background('#FFFFFF')
        for thing in self.thingys:
            thing.draw()

    def update(self):
        for i in range(len(self.thingys) - 1):
            for j in range(i+1, len(self.thingys)):
                t1 = self.thingys[i]
                t2 = self.thingys[j]
                
                t1.bounce(t2)
                t2.bounce(t1)
                
        for thing in self.thingys:
            thing.update()

world = World(20)
            
def setup():
    size(XMAX, YMAX)
    background('#FFFFFF')
   
def draw():
    world.update()
    world.draw()