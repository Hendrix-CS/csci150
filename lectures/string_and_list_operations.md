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

# Concatenation

Strings and lists can be concatenated -- that is, you can "glue" two or more together using `+`.

If `s = "example"` and `v = "hello"` then `s + v = "examplehello"`.

Likewise, if `lst = [7, 2, -5]` and `mst = [11, 3, 3, 8]` then `lst + mst = [7, 2, -5, 11, 3, 3, 8]`.

You can make multiple concatenated copies of a string or list by multiplication:

`s * 3 = "exampleexampleexample"` and `lst * 3 = [7, 2, -5, 7, 2, -5, 7, 2, -5]`.

In all of these cases, the original string or list is left unchanged.

# String Methods

The following are common built-in methods which act on strings.

* `s.lower()` returns a new string where any upper-case alphabetic characters are replaced with their lower-case equivalent.
Other characters (spaces, punctuation, emojis, whatever) are left alone.

* `s.upper()` returns a new string where any lower-case alphabetic characters are replaced with their upper-case equivalent.

* `s.isdigit()` returns the boolean `True` is each character of `s` is a digit and `False` otherwise. Note that `"-12".isdigit()` returns `False` since the negative sign is not a digit.

* `s.count(t: str)` returns an integer count of the number of occurrences of `t` within `s`.

* `s.find(t: str)` returns the integer index of the first occurrence of `t` in `s`. If `t` is not present, it returns `-1`.

* `s.replace(t: str, u: str)` returns a new string where each occurrence of `t` is replaced with `u`.



**Immutability:** Note that the first two and last three return new strings as their value, but do not change the string `s`. Strings are immutable.

# List methods

The following are common built-in methods which act on lists.

* `lst.count(item)` returns an integer count of the number of occurrences of `item` within the elements of `lst`.

* `list.index(item)` returns the integer index of the first occurrence of `item` within `lst`. If `item` is not in `lst` it throws a `value error`.

* `lst.remove(item)` changes `lst` so that the first occurrence of `item` is removed. If `item` is not in `lst`, it throws a `value error`.

* `lst.pop(i: int)` changes `lst` by removing the entry in index `i`. This entry is returned as well. Throws an `index error` if `i` is not a valid index for `lst`.

* `lst.append(item)` changes `lst` by adding `item` to the end of the list.

**Mutability:** Unlike strings, lists *are* mutable. Notice that each of `remove()`, `pop()`, and `append()` change the value of the list. In addition, you can explicitly change a particular index directly -- `lst[2] = 123` will change the value of `lst` to `[7, 2, 123]`. You cannot change a string in this way: `s[2] = "b"` will not produce "exbmple" but instead an error.

# Split and Join

These two combine strings and lists:

* `s.split(t: str)` returns a new *list* based on `s` where `t` is the delimiter -- that is, each occurrence of `t` is the "signpost" to stop and start a new entry in the list. For example, `"abcahcarcctt".split("c")` returns `['ab', 'ah', 'ar', '', 'tt']`.

* `s.join(lst)` will return a single string which puts a copy of `s` between each entry of `lst`. For example, `",".join(["ab","hi there", "bye"])` will return `"ab,hi there,bye"`. Note that `join` will only work if the elements of `lst` are themselves strings.
