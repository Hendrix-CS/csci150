from typing import *

# Print the items in the list, one per line
def explode_list(items: List[str]):
    i: int = 0
    while i < len(items):
        print(items[i])
        i += 1
