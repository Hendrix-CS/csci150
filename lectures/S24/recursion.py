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
