# A tiny language model.

# First version:
# Want to build a dictionary that records what letters might come next after each letter.
# i.e.  dict[str, dict[str, float]]

# e.g.   {'t': {'e': 0.2, 'h': 0.6, 'a': 0.2}, 'p': {'r': 0.1, .... }, .....}
#   After t, we saw e, h, and a with the above probabilities; after p we saw r, ...
#
# 1. Create such a dictionary from some training data
# 2. Use the dictionary to generate new text by picking each letter randomly according to the given probabilities
#    of what could come next at each step.

import random

def normalize(counts: dict[str, int]) -> dict[str, float]:
    total = 0
    for c in counts:
        total += counts[c]

    freqs: dict[str, float] = {}
    for c in counts:
        freqs[c] = counts[c] / total

    return freqs

def train(text: str, k: int) -> dict[str, dict[str, float]]:
    counts: dict[str, dict[str, int]] = {}

    prev = text[:k]
    for next in text[k:]:
        if prev not in counts:
            counts[prev] = {}
        if next not in counts[prev]:
            counts[prev][next] = 0
        counts[prev][next] += 1

        prev = prev[1:] + next

    for c in counts:
        counts[c] = normalize(counts[c])
    return counts

def choose(freq: dict[str, float]) -> str:
    r = random.random()
    total = 0
    for k in freq:
        total += freq[k]
        if total >= r:
            return k

def generate(freqs: dict[str, dict[str, float]], prompt: str, k: int, n: int) -> str:
    for i in range(n):
        last = prompt[-k:]
        next = choose(freqs[last])
        prompt += next

    return prompt