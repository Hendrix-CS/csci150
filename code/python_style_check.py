#! /usr/bin/env python

#
# A simple-minded style checker for python code.
# This only catches the most obvious errors.
#

import os.path, sys, string, re

#
# Constants.
#

MAX_LINE_LENGTH = 78

#
# Regular expressions corresponding to style violations.
#

tabs                = re.compile(r"\t+")
comma_space         = re.compile(",[^ \n]")

# This one is really tough to get right, so we settle for catching the
# most common mistakes.  Add other operators as necessary and/or feasible.
# I added support for parens/brackets on either side of the operator.
# I removed the "-" operator because it causes too many problems
# (unary minus, ranges in comments).  Sigh.
non_operator        = "(\w|\)|\(|\[|\])"
operator1           = "\+|\*|\<|\>|\="
operator2           = "\=\=|\<\=|\>\="
operator_space_str  = "((%s)(%s)(%s))|(%s(%s)(%s))" % \
                      (non_operator, operator1, non_operator,
                       non_operator, operator2, non_operator)
operator_space      = re.compile(operator_space_str)
comment_line        = re.compile("^\s*#.*")
open_comment_space  = re.compile("#[^ \n#!]")


def check_line(filename, line, n):
    """
    Check a line of code for style mistakes.
    """
    # Strip the terminal newline.
    line = line[:-1]

    if tabs.search(line):
        print "File %s, line %d: [TABS]:\n%s" % \
              (filename, n, line)
    if len(line) > MAX_LINE_LENGTH:
        print "File %s, line %d: [LINE IS TOO LONG (%d CHARS)]:\n%s" % \
              (filename, n, len(line), line)
    if comma_space.search(line):
        print "File %s, line %d: [PUT SPACE AFTER COMMA]:\n%s" % \
              (filename, n, line)
    if operator_space.search(line):
        if not comment_line.search(line):
            print "File %s, line %d: [PUT SPACE AROUND OPERATORS]:\n%s" % \
                  (filename, n, line)
    if open_comment_space.search(line):
        print "File %s, line %d: [PUT SPACE AFTER OPEN COMMENT]:\n%s" % \
              (filename, n, line)


def check_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):
        check_line(filename, lines[i], i + 1)  # Start on line 1.


#
# Main body of program.
#
valid = False
while not valid:
    file = raw_input("What file would you like to check for Python style? ")
    if os.path.isfile(file):
        check_file(file)
        valid = True
    else:
        print "Invalid file name, please try again."
print "Thank you for using the style checker."
