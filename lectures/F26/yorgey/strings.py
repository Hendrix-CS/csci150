# String practice!

# Print each character of a string on a separate line.
#
# e.g.  explode('hello') should print out
#
# h
# e
# l
# l
# o
#
def explode(s: str):
    pos = 0
    while pos < len(s):
        print(s[pos])
        pos += 1

# Count the number of digits in the string s.
#
# e.g.  count_digits('hello, 150!') == 3
#
# remember you can check whether something is a digit with   d.isdigit()
def count_digits(s: str) -> int:
    i = 0
    digit_count = 0
    while i < len(s):
        if '0' <= s[i] <= '9':   # or   if s[i].isdigit()
            digit_count += 1
        i += 1

    return digit_count