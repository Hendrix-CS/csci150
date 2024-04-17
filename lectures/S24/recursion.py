def vowel_count_for(s: str) -> int:
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
    return count


def vowel_count(s: str) -> int:
    count = 0
    while len(s) > 0:
        if s[0] in 'aeiou':
            count += 1
        s = s[1:]
    return count


# Recursion
def vowel_count_r(s: str) -> int:
    if len(s) > 0:
        count = vowel_count_r(s[1:]) # Recursive function call
        if s[0] in 'aeiou':
            count += 1
        return count
    else:
        return 0


import os, os.path


def recursive_file_count(filename: str) -> int:
    if os.path.isdir(filename):
        count = 0
        for file in os.listdir(filename):
            count += recursive_file_count(f"{filename}/{file}")
        return count
    else:
        return 1


def factorial(n: int) -> int:
    if n < 0:
        print("You can't do that!")
    elif n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# Recursively define addition, given that our only
# operator is to add 1 or subtract 1.
def add(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return 1 + add(a, b - 1)


# Recursively define multiplication, given addition
def times(a: int, b: int) -> int:
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + times(a, b - 1)


def count_letter(s: str, letter: str) -> int:
    if s == '':
        return 0
    elif s[0] == letter:
        return 1 + count_letter(s[1:], letter)
    else:
        return count_letter(s[1:], letter)


def retain_if(s: str, letters_to_keep: str) -> str:
    if s == '':
        return ''
    elif s[0] in letters_to_keep:
        return s[0] + retain_if(s[1:], letters_to_keep)
    else:
        return retain_if(s[1:], letters_to_keep)


def has_double_letter(s: str) -> bool:
    if len(s) < 2:
        return False
    elif s[0] == s[1]:
        return True
    else:
        return has_double_letter(s[1:])