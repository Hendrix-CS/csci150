from graphics import *
import random

class Ship:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.r = Rectangle(Point(self.x - 20, self.y - 20),
                           Point(self.x, self.y + 20))
        self.r.setFill("#FF0000")

    def draw(self, win):
        self.r.draw(win)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.r.move(dx, dy)

class Explosion:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.c = Circle(Point(self.x, self.y), 10)
        self.c.setFill("#00FFFF")

    def draw(self, win:GraphWin):
        self.c.draw(win)

    def update(self, win:GraphWin) -> bool:
        if self.c.getRadius() < 60:
            self.c.undraw()
            self.c = Circle(Point(self.x, self.y), self.c.getRadius() + 1)
            self.c.setFill("#00FFFF")
            self.draw(win)
            return True
        else:
            self.c.undraw()
            return False

    def collision(self, other:"Face") -> bool:
        dist = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return dist < self.c.getRadius()


class Face:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.vx = random.random() * 3.0 - 1.5
        self.vy = random.random() * 3.0 - 1.5
        self.c = Circle(Point(self.x, self.y), 10)
        self.r = Rectangle(Point(self.x - 20, self.y - 20),
                           Point(self.x, self.y + 20))
        self.s = Line(Point(self.x - 40, self.y),
                      Point(self.x + 20, self.y + 10))

    def draw(self, win:GraphWin):
        self.c.draw(win)
        self.r.draw(win)
        self.s.draw(win)

    def undraw(self):
        self.c.undraw()
        self.r.undraw()
        self.s.undraw()

    def update(self, win:GraphWin):
        if self.x + self.vx >= win.getWidth() or self.x + self.vx <= 0:
            self.vx *= -1
        if self.y + self.vy >= win.getHeight() or self.y + self.vy <= 0:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy
        self.c.move(self.vx, self.vy)
        self.r.move(self.vx, self.vy)
        self.s.move(self.vx, self.vy)


def main():
    win = GraphWin("My Circle", 640, 480, autoflush=False)

    faces = []
    for i in range(10):
        faces.append(Face(random.randint(40, 600), random.randint(40, 440)))

    for f in faces:
        f.draw(win)

    explosions = []

    ship = Ship(320, 240)
    ship.draw(win)

    # Big Animation Loop
    while True:
        for f in faces:
            f.update(win)

        clickPoint = win.checkMouse()
        if clickPoint is not None:
            e = Explosion(clickPoint.getX(), clickPoint.getY())
            e.draw(win)
            explosions.append(e)

        i = 0
        while i < len(explosions):
            e = explosions[i]
            worked = e.update(win)
            if not worked:
                explosions.pop(i)
            else:
                i += 1

        for e in explosions:
            for f in faces:
                if e.collision(f):
                    f.undraw()

        keyString = win.checkKey()
        if keyString.upper() == "W":
            ship.move(0, -10)
        elif keyString.upper() == "A":
            ship.move(-10, 0)
        elif keyString.upper() == "S":
            ship.move(0, 10)
        elif keyString.upper() == "D":
            ship.move(10, 0)
        elif keyString.upper() == "F":
            e = Explosion(ship.x, ship.y)
            e.draw(win)
            explosions.append(e)

        update(30)

    win.getMouse()
    win.close()

main()
