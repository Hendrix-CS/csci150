def f(n: int) -> str:
    n = 2 * n + 1
    return str(n)

def g(n: int):
    s = f(n) + f(n+2)
    print(s)
    print("n is " + str(n))

def main():
    g(7)
    g(2)

main()

def q(n: int) -> str:
    s = 'TIPNR'
    return s[n % 5]

def m():
    i = 2
    count = 0
    s = ''
    while count < 5:
        s += q(i)
        i += 2
        count += 1
    print(s)

m()

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

