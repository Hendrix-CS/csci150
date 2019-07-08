import math

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

class Circle:
    def __init__(self, init_x, init_y, init_radius, init_vx, init_vy):
        self.pos = Vector(init_x, init_y)
        self.r = init_radius
        
        self.v = Vector(init_vx, init_vy)
        
        self.update_count = 0
        self.cur_number = 0

    def draw(self):
        fill(100, 100, random(150, 200))        
        ellipse(self.pos.x, self.pos.y, 2*self.r, 2*self.r)
        fill('#55ff55')
        text(str(self.cur_number), self.pos.x, self.pos.y)
        # text("Have a lovely day!", self.x, self.y)
        
    def update(self):
        self.update_count += 1
        if self.update_count == 100:
            self.change_number()
            self.update_count = 0
        
        # Make it wibbly
        # self.vx += random(-0.5, 0.5)
        # self.vy += random(-0.5, 0.5)
        
        if self.pos.y + self.r >= height:
            self.v.y = -self.v.y
        if self.pos.y - self.r <= 0:
            self.v.y = -self.v.y
        if self.pos.x + self.r >= width:
            self.v.x = -self.v.x
        if self.pos.x - self.r <= 0:
            self.v.x = -self.v.x
        
        self.pos.x += self.v.x
        self.pos.y += self.v.y
        
    def intersect(self, other):
        return dist(self.pos, other.pos) <= (self.r + other.r)
        
    def bounce(self, other):
        if (self.intersect(other)):
            
            m1 = self.r**2
            m2 = other.r**2
            
            u1 = self.v.copy()
            u2 = other.v.copy()
            
            self.v = (u1.scaled(m1 - m2) + u2.scaled(2*m2)).scaled(1/(m1 + m2))
            other.v = (u2.scaled(m2 - m1) + u1.scaled(2*m1)).scaled(1/(m1 + m2))
        
    def change_number(self):
        self.cur_number = int(random(0, 1000))

class World:
    def __init__(self):
        self.circles = []
        self.circles.append(Circle(100, 100, 40, 1, 0.8))
        self.circles.append(Circle(500, 200, 60, -1, 0.8))
        
    def add_circle(self, x, y):
        self.circles.append(Circle(x, y, random(10, 100), random(-1, 1), random(-1, 1)))
        
    def update(self):
        for i in range(len(self.circles) - 1):
            for j in range(i+1, len(self.circles)):
                bi = self.circles[i]
                bj = self.circles[j]
                bi.bounce(bj)

        for c in self.circles:
            c.update()
            
        
    def draw(self):
        for c in self.circles:
            c.draw()

# c = Circle(100, 100, 40, 1, 0.8)
w = World()

def setup():
    textSize(16)
    size(600, 600)

def draw():
    background('#ffffff')
    w.update()
    w.draw()
    
def mouseClicked():
    w.add_circle(mouseX, mouseY)
    
