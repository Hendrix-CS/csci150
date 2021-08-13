# Seymour Papert
import math
from turtle import *

def main():
    t = Turtle()
    t.speed(0)
    t.penup()
    t.goto(-300,-250)
    t.pendown()
    sierpiński(t, 600, 8, True)

    input("")

def koch(t: Turtle, size: float, n: int):
    if n == 0:
        t.forward(size)
    else:
        koch(t, size/3, n-1)
        t.left(60)
        koch(t, size/3, n-1)
        t.right(120)
        koch(t, size/3, n-1)
        t.left(60)
        koch(t, size/3, n-1)

def dragon(t: Turtle, size: float, n: int, blue: bool):
    if n == 0:
        t.forward(size)
    else:
        multiplier = 1
        if not blue:
            multiplier = -1

        t.right(multiplier * 45)
        dragon(t, size / math.sqrt(2), n-1, True)
        t.left(multiplier * 90)
        dragon(t, size / math.sqrt(2), n-1, False)
        t.right(multiplier * 45)

def sierpiński(t: Turtle, size: float, n: int, blue: bool):
    if n == 0:
        t.forward(size)
    else:
        multiplier = 1
        if not blue:
            multiplier = -1

        sierpiński(t, size/2, n-1, not blue)
        t.right(multiplier * 60)
        sierpiński(t, size/2, n-1, blue)
        t.right(multiplier * 60)
        sierpiński(t, size/2, n-1, not blue)


def square(t: Turtle, size: float):
    for _ in range(4):
        t.forward(size)
        t.left(90)

main()