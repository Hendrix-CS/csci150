---
layout: work
type: Homework
num: 10
worktitle: Dictionaries
---

Write two functions:
1. The first function, `vowel_histogram(s: str) -> Dict[str,int]`, should return a dictionary
where the keys are vowels (a, e, i, o, u) and the values are the number of occurrences of each
vowel in the string. Here is an example of calling the function in the console:

```
>>> vowel_histogram('This restaurant is a long way from our house.')
{'a': 4, 'e': 2, 'i': 2, 'o': 4, 'u': 3}
```

2. The second function, `min_key(d: Dict[str, int]) -> str`, should return the key in the 
dictionary with the smallest value. Here is an example of calling the function in the console:

```
>>> min_key({'a': 4, 'b': -5, 'c': 2, 'd': -7, 'e': 4})
'd'
```
