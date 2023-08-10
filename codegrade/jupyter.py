import json
import sys
import argparse
from pathlib import Path

# Add tag as comment to the code cells that you want to grade, e.g.:
# In code cell: #CodeGrade Tag step1
# The step behind the tag is the tag that is looked for and that is given as
# an argment to python3 jupyter.py.



TEST_TAG = "CodeGrade Tag"

def walk_cells(data, tag, ignore=None, test_tag=TEST_TAG):
    """
    Walk through all cells of the notebook, combining all code cells until the
    given tag was found (inclusive). If an ignore tag is given, the code cell
    with that tag will be left out.
    """
    cells = []
    for cell in data["cells"]:
        if cell["cell_type"] == "code":
            add_cell = True
            for line in cell["source"]:
                if test_tag in line and tag in line:
                    cells.append(cell["source"])
                    return cells
                if ignore:
                    if test_tag in line and ignore in line:
                        add_cell = False
            if add_cell:
                cells.append(cell["source"])

    return []

def convert_lines(cell, wrap_print):
    """
    Returns string of all lines in a code cell, if `wrap_print` is True it
    wraps the last line in a print statement.
    (In Jupyter Notebooks, no print statement is needed to print out the
    result of the last line in a cell, but after converting to Python code
    a print statement is needed to print out that result.)
    """
    string = ""
    for line in cell[:-1]:
        string += line

    if wrap_print:
        string += "print(" + cell[-1] +")\n"
    else:
        string += cell[-1] + "\n"

    return string

def to_string(cells, execute_all, wrap_print):
    """
    Given all code cells, returns a string of all Python code in those cells.
    If `execute_all` is True, all code cells are added to this string, if not
    only the last one is added.
    If `wrap_print` is True, the last line of the last code cell is wrapped
    in a print statement. See `convert_lines()` for more info.
    """
    string = ""
    if execute_all:
        for cell in cells[:-1]:
            string += convert_lines(cell, False)
            string += "\n"
    string += convert_lines(cells[-1], wrap_print)

    return string


parser = argparse.ArgumentParser(description='Parse Jupyter Notebook and convert cells to Python to run (up to) individual cells')

parser.add_argument('jupyter_file', type=str)
parser.add_argument('tag', type=str)
parser.add_argument('--ignore', type=str)
parser.add_argument('--custom_test_tag', type=str)
parser.add_argument('--execute_all', action='store_true')
parser.add_argument('--wrap_print', action='store_true')
parser.add_argument('--to_file', action='store_true')
parser.set_defaults(execute_all=False, to_file=False, wrap_print=False, custom_test_tag=TEST_TAG)

args = parser.parse_args()

with open(args.jupyter_file) as f:
    if args.ignore:
        cells = walk_cells(json.load(f), args.tag, ignore=args.ignore, test_tag=args.custom_test_tag)
    else:
        cells = walk_cells(json.load(f), args.tag, test_tag=args.custom_test_tag)

if len(cells) == 0:
    print('Tag not found, do not remove comments with "' + args.custom_test_tag + '" from the notebook cells.')
    exit(1)

python_string = to_string(cells, args.execute_all, args.wrap_print)

if args.to_file:
    with open(Path(args.tag + '.py'), 'w') as f:
        f.write(python_string)
else:
    program = compile(python_string, 'temp', 'exec')
    exec(program, globals(), locals())