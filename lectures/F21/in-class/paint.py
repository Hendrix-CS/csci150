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

    def inside(self, rect: Rect) -> bool:
        for p in self.points:
            if not rect.contains(p):
                return False
        return True

    def move(self, v: Tuple[int, int]):
        for i in range(len(self.points)):
            self.points[i] = \
                (self.points[i][0] + v[0], self.points[i][1] + v[1])

    def copy(self):
        return Stroke(self.points.copy(), self.color, self.stroke_width)

@dataclass
class Rect:
    ul: Tuple[int, int]
    lr: Tuple[int, int]
    color: str
    stroke_width: int

    def update(self, p: Tuple[int,int]):
        self.lr = p

    def draw(self, surface):
        w: int = self.lr[0] - self.ul[0]
        h: int = self.lr[1] - self.ul[1]
        pygame.draw.rect(surface, self.color, (self.ul, (w, h)), self.stroke_width)

    def contains(self, p: Tuple[int, int]) -> bool:
        return self.ul[0] <= p[0] <= self.lr[0] and self.ul[1] <= p[1] <= self.lr[1]

    def inside(self, rect: 'Rect') -> bool:
        return rect.contains(self.ul) and rect.contains(self.lr)

    def move(self, v: Tuple[int, int]):
        self.ul = (self.ul[0] + v[0], self.ul[1] + v[1])
        self.lr = (self.lr[0] + v[0], self.lr[1] + v[1])

    def copy(self):
        return Rect(self.ul, self.lr, self.color, self.stroke_width)

@dataclass
class Line:
    start: Tuple[int, int]
    end: Tuple[int, int]
    color: str
    stroke_width: int

    def update(self, p: Tuple[int,int]):
        self.end = p

    def draw(self, surface):
        pygame.draw.line(surface,self.color,self.start,self.end,self.stroke_width)

    def inside(self, rect: Rect) -> bool:
        return rect.contains(self.start) and rect.contains(self.end)

    def move(self, v: Tuple[int, int]):
        self.start = (self.start[0] + v[0], self.start[1] + v[1])
        self.end = (self.end[0] + v[0], self.end[1] + v[1])

    def copy(self):
        return Line(self.start, self.end, self.color, self.stroke_width)

@dataclass
class Group:
    things: list

    def append(self, thing):
        self.things.append(thing)

    def pop(self):
        return self.things.pop()

    def draw(self, surface):
        for thing in self.things:
            thing.draw(surface)

    def __len__(self) -> int:
        return len(self.things)

    def select(self, rect: Rect) -> 'Group':
        g = Group([])
        for thing in self.things:
            if thing.inside(rect):
                g.append(thing.copy())
        return g

    def move(self, v: Tuple[int,int]):
        for thing in self.things:
            thing.move(v)

@dataclass
class Moving:
    thing: Any
    old_point: Tuple[int, int]

    def update(self, new_point: Tuple[int, int]):
        v = (new_point[0] - self.old_point[0], new_point[1] - self.old_point[1])
        self.thing.move(v)
        self.old_point = new_point

    def draw(self, surface):
        self.thing.draw(surface)


# PaintState keeps track of the current state of our
# paint program
@dataclass
class PaintState:
    surface: pygame.Surface
    things: Group
    undone_things: Group
    selected: Group = None
    cur_thing = None
    stroke_width: int = 1

    select_mode: bool = False
    paste_mode: bool = False

    cur_tool: str = 'pencil'
    cur_color: str = 'black'

    def draw(self):
        self.surface.fill('white')
        self.things.draw(self.surface)

        if self.select_mode or self.paste_mode:
            self.cur_thing.draw(self.surface)

        pygame.display.update()


    # Create a new thing starting at location p
    def new_thing(self, p: Tuple[int, int]):
        # Make a new, empty stroke
        if self.cur_tool == 'pencil':
            self.cur_thing = Stroke([], self.cur_color, self.stroke_width)
        elif self.cur_tool == 'rect':
            self.cur_thing = Rect(p, p, self.cur_color, self.stroke_width)
        elif self.cur_tool == 'line':
            self.cur_thing = Line(p, p, self.cur_color, self.stroke_width)
        elif self.cur_tool == 'select':
            self.cur_thing = Rect(p, p, 'black', 1)
            self.select_mode = True
        elif self.cur_tool == 'paste':
            if self.selected is not None:
                self.cur_thing = Moving(self.selected, p)
            self.paste_mode = True

        # Set the initial (x,y) coordinates
        self.cur_thing.update(p)

        # Add the new current thing to the list of
        # all things.
        if self.cur_tool != 'select' and self.cur_tool != 'paste':
            self.things.append(self.cur_thing)

    # Update the position of the mouse while dragging
    def update(self, p: Tuple[int,int]):
        self.cur_thing.update(p)

    def finish(self):
        if self.select_mode:
            self.selected = self.things.select(self.cur_thing)
            self.select_mode = False
        elif self.paste_mode:
            for thing in self.cur_thing.thing.things:
                self.things.append(thing)
            self.paste_mode = False

    def set_stroke_width(self, w: int):
        self.stroke_width = w

    def set_tool(self, tool: str):
        self.cur_tool = tool

    def set_color(self, color: str):
        self.cur_color = color

    def undo(self):
        if len(self.things) > 0:
            thing = self.things.pop()
            self.undone_things.append(thing)

    def redo(self):
        if len(self.undone_things) > 0:
            thing = self.undone_things.pop()
            self.things.append(thing)

def main():
    pygame.init()

    surface = pygame.display.set_mode((640, 400))
    state: PaintState = PaintState(surface, Group([]), Group([]))

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
                state.finish()
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
                elif key in color_dict:
                    color: str = color_dict[key]
                    state.set_color(color)
                    print(f'Setting color to {color}...')
                elif key == 'q':
                    running = False
            elif event.type == KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    state.undo()
                elif event.key == pygame.K_TAB:
                    state.redo()

    pygame.quit()

color_dict: Dict[str, str] = {
    'R': 'red',
    'O': 'orange',
    'Y': 'yellow',
    'G': 'green',
    'B': 'blue',
    'P': 'purple',
    'N': 'pink',
    'K': 'black'
}

tool_dict: Dict[str, str] = {
    'p': 'pencil',
    'r': 'rect',
    'l': 'line',
    's': 'select',
    'v': 'paste'
}

if __name__ == '__main__':
    main()

