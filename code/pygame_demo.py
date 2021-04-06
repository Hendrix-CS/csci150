import math

import pygame

from pygame.locals import *
from dataclasses import dataclass
from typing import *


@dataclass
class Stroke:
    points: List[Tuple[int, int]]
    stroke_width: int
    color: str

    def update(self, p: Tuple[int, int]):
        self.points.append(p)

    def draw(self, surface):
        if len(self.points) >= 2:
            pygame.draw.lines(surface, self.color, False, self.points, self.stroke_width)


@dataclass
class Rectangle:
    ul: Tuple[int, int]
    lr: Tuple[int, int]
    stroke_width: int
    color: str

    def update(self, p: Tuple[int, int]):
        self.lr = p

    def draw(self, surface):
        w: int = self.lr[0] - self.ul[0]
        h: int = self.lr[1] - self.ul[1]
        pygame.draw.rect(surface, self.color, (self.ul, (w,h)), self.stroke_width)


@dataclass
class Circle:
    center: Tuple[int, int]
    radius: float
    stroke_width: int
    color: str

    def update(self, p: Tuple[int, int]):
        self.radius = math.sqrt((self.center[0] - p[0])**2 + (self.center[1] - p[1])**2)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius, self.stroke_width)


@dataclass
class PaintState:
    shapes: list
    cur_thing = None
    cur_stroke_width: int = 1
    cur_color: str = 'black'
    cur_tool: str = 'pencil'

    def add_shape(self, shape):
        self.shapes.append(shape)

    def clear(self):
        self.shapes = []

    def new_thing(self, p: Tuple[int, int]):
        if self.cur_tool == 'pencil':
            self.cur_thing = Stroke([p], self.cur_stroke_width, self.cur_color)
        elif self.cur_tool == 'rectangle':
            self.cur_thing = Rectangle(p, p, self.cur_stroke_width, self.cur_color)
        elif self.cur_tool == 'circle':
            self.cur_thing = Circle(p, 0, self.cur_stroke_width, self.cur_color)

        self.add_shape(self.cur_thing)

    def update_thing(self, p: Tuple[int, int]):
        self.cur_thing.update(p)

    def set_stroke_width(self, w: int):
        self.cur_stroke_width = w

    def set_color(self, color: str):
        self.cur_color = color

    def set_tool(self, tool: str):
        self.cur_tool = tool

    def get_tool(self) -> str:
        return self.cur_tool

    def draw(self, surface):
        surface.fill('white')
        for shape in self.shapes:
            shape.draw(surface)
        pygame.display.update()


tool_dict: Dict[str, str] = \
    {'p': 'pencil',
     'r': 'rectangle',
     'c': 'circle'}

color_dict: Dict[str, str] = \
    {'R': 'red', 'O': 'orange', 'Y': 'yellow',
     'G': 'green', 'B': 'blue', 'P': 'purple',
     'K': 'black', 'W': 'white'}

def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))

    running = True
    drawing = False

    state: PaintState = PaintState([])

    while running:
        state.draw(surface)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                drawing = True
                state.new_thing((event.pos[0], event.pos[1]))
            elif event.type == MOUSEMOTION and drawing:
                state.update_thing((event.pos[0], event.pos[1]))
            elif event.type == MOUSEBUTTONUP:
                drawing = False
            elif event.type == KEYDOWN and event.key == K_DELETE:
                state.clear()
            elif event.type == pygame.TEXTINPUT:
                key: str = event.text
                if key.isdigit():
                    w: int = int(key)
                    state.set_stroke_width(w)
                    print(f'Setting stroke width to {w}...')
                elif key in tool_dict:
                    print(f'Setting drawing tool to: {tool_dict[key]}')
                    state.set_tool(tool_dict[key])
                elif key in color_dict:
                    print(f'Setting color to: {color_dict[key]}')
                    state.set_color(color_dict[key])
    pygame.quit()


if __name__ == '__main__':
    main()
