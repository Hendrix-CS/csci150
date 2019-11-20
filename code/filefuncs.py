from typing import *
import os

# EXPLAIN ME
def files_and_folders(path: str):
    i: int = 0
    files: List[str] = os.listdir(path)
    for f in files:
        child: str = path + os.sep + f
        if os.path.isdir(child):
            print(child + " is a folder")
        else:
            print(child + " is a regular file")
        i += 1


def find_depth(path: str) -> int:
    pass
    # set an integer variable representing the deepest path to zero
    # for each file in the current folder
        # If it is a folder
          # Call find_depth recursively on that folder, storing the result in a variable.
          # If the returned value, plus 1, is greater than our deepest path so far,
          #   set our deepest path to be that value. Otherwise, do nothing.
    # return the deepest path


def file_count(path: str) -> int:
    pass
    # set an integer variable representing the total number of files to zero
    # for each file in the current folder
        # If it is a folder
          # Call file_count recursively on that folder, adding the result to our total
        # Otherwise
          # Add 1 to our total
    # return the total


def all_files_with(path: str, target_string: str) -> List[str]:
    pass
    # set a variable representing all the filenames containing target_string to the empty list
    # for each file in the current folder
        # If it is a folder
          # Call all_files_with on that folder, adding every element from the list it returns
          #  to our own list.
        # Otherwise
          # Open the file and read it into a string.
          # If the string contains our target_string, add the filename to our list.
    # return our list of filenames
