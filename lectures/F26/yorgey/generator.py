import random

def dict_sum(counts: dict[str, int]) -> int:
    sum = 0
    for k in counts:   # a for loop on a dictionary will loop through all the keys.
        sum += counts[k]
    return sum

def normalize(counts: dict[str, int]) -> dict[str, float]:
    # (1) call dict_sum to find out the total
    total = dict_sum(counts)
    # (2) create a new empty dictionary to hold the normalized frequencies
    freq_dict: dict[str, float] = {}
    # (3) loop through counts, put each key in the new dict with a normalized value (divide by total)
    for k in counts:
        freq_dict[k] = counts[k] / total

    # (4) return the new dict
    return freq_dict

def choose(weights: dict[str, float]) -> str:
    r = random.random()
    total = 0
    for k in weights:
        total += weights[k]
        if r < total:
            return k

def main():
    file = open('alice-chapter-one.txt', 'r')
    chapter = file.read()
    file.close()

    # Each letter is associated to a dictionary recording
    # which letters came after and how often each occurred.
    counts: dict[str, dict[str, int]] = {}

    for i in range(len(chapter) - 1):
        c = chapter[i]
        next = chapter[i+1]
        if c not in counts:
            counts[c] = {}

        if next not in counts[c]:
            counts[c][next] = 0

        counts[c][next] += 1

    freqs: dict[str, dict[str, float]] = {}
    for c in counts:
        freqs[c] = normalize(counts[c])

    cur = 'f'
    output = []

    for i in range(1000):
        output.append(cur)
        cur = choose(freqs[cur])

    print(''.join(output))

main()