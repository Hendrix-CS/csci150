from typing import *

def aaa(words: List[str]) -> Dict[str, int]:
    d = {}
    for w in words:
        if w[0] not in d:
            d[w[0]] = 0
        d[w[0]] += 1

    return d

def main():
    dict = aaa(['aardvark', 'apple', 'bear', 'fish', 'ant'])
    print(dict['a'])

def bbb(d: Dict[str, str]) -> Dict[str, List[str]]:
    mystery = {}
    for word in d:
        if d[word] not in mystery:
            mystery[d[word]] = []
        mystery[d[word]].append(word)
    return mystery

def main2():
    wordmap = {'hi':'there', 'whoa':'there'}
    wordmap['whoa'] = 'nelly'
    wordmap['you']  = 'there'
    print(bbb(wordmap))


def f(nums: List[int]) -> List[int]:
    nums[1] += 5
    nums = [6,7]
    nums[0] *= 2
    return nums

def g(ns: List[int]):
    print(ns)
    f(ns)
    print(ns)

def main3():
    mylist = [6,1,5,2]
    g([3] + mylist)
    print(mylist[0])
