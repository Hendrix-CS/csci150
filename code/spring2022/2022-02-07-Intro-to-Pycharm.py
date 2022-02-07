# Notes for class:
# * remember that Homework #4 -- CodingBat conditional & By-Hand tracing is due on Wednesday, Feb 9
# * Practice Exam #1 is posted on the course website -- we will go over it on Friday as review
# * Exam #1 takes place next week:
#    --  In class on Monday, covers Booleans, tracing, simple code-writing (all by hand)
#    --  Take home due on Wednesday: you will write 4 functions in Kaggle (or Pycharm if you prefer)




# This is the first Pycharm file that we will write

# Unlike Kaggle, Python will interpret the entire file at once, rather than cell-by-cell
# There are advantages and disadvantages to both -- professional programmers typically
# use a mix of cell-based notebooks and text-editor, IDE software, depending on their use case

# To set up Pycharm correct, choose 'New Project'from the File menu.
# You can name the project whatever you'd like, and put it anywhere in your directory structure.
# Make sure that you choose Python 3.10 (or 3.9, if that is what is installed on your machine) as your interpreter
# Some older machines -- especially Macs -- may have Python 2.7 pre-installed.
# Though Python 2.7 is very nice, it has some significant differences from Python 3 and you will
# quickly become hopelessly confused.


print('Hello world')

def py_test(a: int, b: int) -> int:
    if a < b:
        return a + b
    else:
        return b


# Pycharm has two options to run code:
#  * 'Run', from the top menu will run everything.
# * 'Run File in the Python Console'is also very useful. On  PC, right click inside the
#      file and you'll see it   option. On  Mac, you have to do the two-finger tap thing