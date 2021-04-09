import pygame
from pygame.locals import *
from dataclasses import dataclass
from typing import *
import random

@dataclass
class Stroke:
    points: List[Tuple[int, int]]
    color: str
    stroke_width: int

    def update(self, p: Tuple[int,int]):
        self.points.append(p)

    def draw(self, surface):
        if len(self.points) >= 2:
            pygame.draw.lines(surface, self.color, False, self.points, self.stroke_width)

@dataclass
class Rect:
    upper_left: Tuple[int,int]
    lower_right: Tuple[int,int]
    color: str
    stroke_width: int

    def update(self, p: Tuple[int,int]):
        self.lower_right = p

    def draw(self, surface):
        w: int = self.lower_right[0] - self.upper_left[0]
        h: int = self.lower_right[1] - self.upper_left[1]
        pygame.draw.rect(surface, self.color, (self.upper_left, (w,h)), self.stroke_width)

# PaintState keeps track of the current state of our
# paint program
@dataclass
class PaintState:
    surface: pygame.Surface
    things: list
    cur_thing = None
    stroke_width: int = 1

    cur_tool: str = 'pencil'

    def draw(self):
        self.surface.fill('white')
        for stroke in self.things:
            stroke.draw(self.surface)

        pygame.display.update()


    # Create a new stroke starting at location p
    def new_thing(self, p: Tuple[int, int]):
        # Make a new, empty stroke
        if self.cur_tool == 'pencil':
            self.cur_thing = Stroke([], random.choice(color_list), self.stroke_width)
        elif self.cur_tool == 'rect':
            self.cur_thing = Rect(p, p, 'black', self.stroke_width)

        # Add the current (x,y) coordinates to the stroke
        self.cur_thing.update(p)

        # Add the new current stroke to the list of
        # all strokes.
        self.things.append(self.cur_thing)

    # Update the position of the mouse while dragging
    def update(self, p: Tuple[int,int]):
        self.cur_thing.update(p)

    def set_stroke_width(self, w: int):
        self.stroke_width = w

    def set_tool(self, tool: str):
        self.cur_tool = tool

def main():
    pygame.init()

    surface = pygame.display.set_mode((640, 400))
    state: PaintState = PaintState(surface, [])

    running = True

    # Are we currently drawing a stroke?
    drawing = False

    while running:
        state.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                drawing = True
                state.new_thing(event.pos)
            elif event.type == MOUSEMOTION:
                if drawing:
                    state.update(event.pos)
            elif event.type == MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.TEXTINPUT:
                key: str = event.text
                if key.isdigit():
                    w: int = int(key)
                    state.set_stroke_width(w)
                    print(f'Setting stroke width to {w}...')
                elif key in tool_dict:
                    tool: str = tool_dict[key]
                    state.set_tool(tool)
                    print(f'Setting drawing tool to {tool}...')

    pygame.quit()

color_list = ['red', 'green', 'blue', 'pink', 'orange']

tool_dict: Dict[str, str] = {
    'p': 'pencil',
    'r': 'rect'
}

if __name__ == '__main__':
    main()

