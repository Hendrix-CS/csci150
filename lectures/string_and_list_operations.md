---
worktitle: Strings and Lists
---

Working with Strings and Lists
# Indexing

Strings and lists are each indexed. In Python, we index starting at 0, so that
in `s = "example"` we see that `s[2] = "a"` and in `lst = [7, 2, -5]` we see that
`lst[2] = -5`.

Negative indices are allowed, where index `-1` is the last character/entry and
index `-2` is the next to last etc.

An `index out of range` error occurs if an index is called that is too large (or too negative),
such as `s[10]` on the string above.

## Slices
A slice of a string or list is a segment which you call as `s[a:b]` or `lst[a:b]`.
In both cases, the slice starts with index `a` and goes up to, but does not include
the element `b`. Thus, `s[1:4] = "xam"` and `lst[0:2] = [7,2]`.

The slice `t[a:]` starts at index `a` and goes to the end of the object `t`.

The slice `t[:b]` starts at the beginning and goes up to, but does not include index `b`.

The slice `t[a:a]` returns the empty string or empty list. Slicing cannot create an
index error. In the above example, `s[100:100]` would simply return the empty string `""`.

## Length
For a string `s` or list `lst`, the built-in Python function `len()` returns an integer
which is the number of characters in the string or elements in the list.

Using our above examples, `len(s) = 7` and `len(lst) = 3`.

# String Methods

The following are common built-in methods which act on strings.

`s.lower()` returns a new string where any upper-case alphabetic characters are replaced with their lower-case equivalent.
Other characters (spaces, punctuation, emojis, whatever) are left alone.

`s.upper()` returns a new string where any lower-case alphabetic characters are replaced with their upper-case equivalent.

`s.digit()` returns the boolean `True` is each character of `s` is a digit and `False` otherwise. Note that `"-12".isdigit()` returns `False` since the negative sign is not a digit.

`s.count(t: str)` returns an integer count of the number of occurrences of `t` within `s`.

`s.find(t: str)` returns the integer index of the first occurrence of `t` in `s`. If `t` is not present, it returns `-1`.

`s.replace(t: str, u: str)` returns a new string where each occurrence of `t` is replaced with `u`.

**Immutability:** Note that the first two and last three return new strings as their value, but do not change the string `s`. Strings are immutable.

# List methods

The following are common built-in methods which act on lists.



    # Input, Sentinel
    finished = False
    while not finished:
        response = input("Enter input: ")
        if response indicates we are finished:
            finished = True
        else:
            # Do other things with response

    # Input, Seeded
    response = seed value; loop condition will be true
    while response indicates we are not finished:
        response = input("Enter input: ")
        # Do other things with response


## Accumulation

    accumulator = identity value for operator and type
    while the loop keeps going:
        accumulator = accumulator [operator] value
        # Do other relevant things

Common types, operators, and identity elements:
* `int`
  * `+`: `0`
  * `*`: `1`
* `float`
  * `+`: `0.0`
  * `*`: `1.0`
* `str`
  * `+`: `''` or `""`
* `List`
  * `.append()`: `[]`


## Mathematical Calculation

    result = appropriate starting value
    while the calculation is not complete:
        update result by one step


## Count until a condition is met

    count = 0
    while condition is not met:
        count += 1
        # other pertinent updates to variables


## Count instances of a property

    count = 0
    while condition is not met:
        if property is true:
            count += 1
        # other stuff

## Check if a property is always true

    always = True
    while always and condition:
        if not property:
            always = False

## Check if a property is ever true

    ever = False
    while not ever and condition:
        if property:
            ever = True


## Traverse a sequence

    i = 0
    while i < len(sequence):
        # Do something with sequence[i]
        i += 1

## Filter a sequence

    new_sequence = empty sequence
    i = 0
    while i < len(sequence):
        if property(sequence[i]):
            add sequence[i] to new_sequence
        i += 1


## Map a sequence

    new_sequence = empty sequence
    i = 0
    while i < len(sequence):
        add transform(sequence[i]) to new_sequence
        i += 1


## Some combinations

    # Accumulate from user inputs
    accumulator = identity element of type and operator
    finished = False
    while not finished:
        value = input("Enter value: ")
        if value indicates we're done:
            finished = True
        else:
            # Transform value to target type if needed
            accumulator = accumulator [operator] value

    # Accumulate from sequence
    accumulator = identity element of type and operator
    i = 0
    while i < len(sequence):
        accumulator = accumulator [operator] sequence[i]
        i += 1

    # Count instances from user inputs
    finished = False
    count = 0
    while not finished:
        response = input("Enter input: ")
        if response indicates we are finished:
            finished = True
        elif response matches our target property:
            count += 1

    # Count instances from a sequence
    count = 0
    i = 0
    while i < len(sequence):
        if sequence[i] matches our target property:
            count += 1
        i += 1

    # Check if a property is true of all elements of a sequence
    always = true
    i = 0
    while always and i < len(sequence):
        if sequence[i] does not match our property:
            always = False
        i += 1

    # Count until a condition is met from input
    finished = False
    count = 0
    while not finished:
        response = input("Enter input: ")
        if response indicates we are finished:
            finished = True
        else:
            count += 1

## Examples

    # Count instances from user inputs
    def count_short_words() -> int:
        count = 0
        finished = False
        while not finished:
            word = input("Enter a word: ")
            if len(word) == 0:
                finished = True
            elif len(word) <= 4:
                count += 1
                print(f"{word} is short!")
            else:
                print(f"{word} is long.")
        return count

    # Accumulate from sequence
    def reverse(s: str) -> str:
        opposite = ''
        i = 0
        while i < len(s):
            opposite = s[i] + opposite
            i += 1
        return opposite

    # Accumulate from sequence
    def smallest_letter(s: str) -> str:
        smallest = s[0]
        i = 1
        while i < len(s):
            if s[i] < smallest:
                smallest = s[i]
            i += 1
        return smallest    

    # Computation
    # Count until a condition is met
    def logarithm(n: int, base: int) -> int:
        count = 0
        while n > 1:
            n //= base
            count += 1
        return count

    # Computation
    def power(base: int, exponent: int) -> int:
        product = 1
        while exponent > 0:
            product *= base
            exponent -= 1
        return product    

    # Traverse a sequence
    def prefixes(s: str):
        i = 0
        while i < len(s):
            print(s[:i+1])
            i += 1

    # Traverse a sequence
    def in_betweens(s: str, length: int):
        i = 0
        while i < len(s) - length + 1:
            print(s[i : i + length])
            i += 1

    # Filter a sequence
    def vowels_only(s: str) -> str:
        vowels = ''
        i = 0
        while i < len(s):
            if s[i] in 'aeiou':
                vowels += s[i]
            i += 1
        return vowels

    # Count instances from a sequence
    def vowel_count(s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            if s[i] in 'aeiou':
                count += 1
            i += 1
        return count

    # Filter a sequence
    def unique_items(items_sold: List[str]) -> List[str]:
        i = 0
        unique = []
        while i < len(items_sold):
            if items_sold[i] not in unique:
                unique.append(items_sold[i])
            i += 1
        return unique

    # Check if a property is true of some elements of a sequence
    def has_vowels(s: str) -> bool:
        ever = False
        i = 0
        while not ever and i < len(s):
            if s[i] in 'aeiou':
                ever = True
            i += 1
        return ever

    # Check if a property is true of all elements of a sequence
    def only_vowels(s: str) -> bool:
        always = True
        i = 0
        while always and i < len(s):
            if s[i] not in 'aeiou':
                always = False
            i += 1
        return always
