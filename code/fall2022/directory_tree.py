from Tree import *

import os

# Return the entire contents of a file/folder as a Tree
def read_thing(path: str) -> Tree:
    t = Tree(path, [])

    if os.path.isdir(path):
        contents = os.listdir(path)
        for thing in contents:
            child = read_thing(path + os.sep + thing)
            t.children.append(child)

    return t

def find_py_files(f: Tree) -> List[str]:
    py_files = []
    if f.value[-3:] == '.py':
        py_files.append(f.value)

    for child in f.children:
        py_files += find_py_files(child)

    return py_files