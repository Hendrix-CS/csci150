def mklist(n):
    nums = []
    i = 0
    p = 1
    while (i <= n):
        nums.append(p)
        p *= 2
        i += 1
    return nums

print(mklist(5))

animals = ['caiman', 'bat', 'dingo', 'chihuahua', 'baboon', 'fox', 'galapagos']

i = 0
while i < len(animals):
    if (animals[i][1] == 'a'):
        print(animals[i])

    i += 1

pos = 0
s = 'thesethickthornythistlethingsthrivethroughoutthethicket'
while pos != -1:
    next = s.find('th',pos+1)
    if next != -1:
        print(s[pos:next])
    else:
        print(s[pos:])
    pos = next

