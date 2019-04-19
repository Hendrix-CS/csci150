
class Circle:
    def __init__(self, init_x, init_y, init_radius, init_vx, init_vy):
        self.x = init_x
        self.y = init_y
        self.r = init_radius
        
        self.vx = init_vx
        self.vy = init_vy

    def draw(self):
        fill(100, 100, random(150, 200))        
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
        fill('#0000ff')
        text("Have a lovely day!", self.x, self.y)
        
    def update(self):
        # Make it wibbly
        self.vx += random(-0.5, 0.5)
        self.vy += random(-0.5, 0.5)
        
        if self.y + self.r >= height:
            self.vy = -self.vy
        if self.y - self.r <= 0:
            self.vy = -self.vy
        if self.x + self.r >= width:
            self.vx = -self.vx
        if self.x - self.r <= 0:
            self.vx = -self.vx
        
        self.x += self.vx
        self.y += self.vy

c = Circle(100, 100, 40, 1, 0.8)

def setup():
    textSize(16)
    size(600, 600)


def draw():
    background('#ffffff')
    c.update()
    c.draw()
