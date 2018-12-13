# Take a number
#   if even, divide by 2
#   if odd, multiply by 3 and add 1
# Keep doing this until reaching 1.

def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def countHailstone(n: int) -> int:
    count = 0
    while n != 1:
        n = hailstone(n)
        count += 1    # count = count + 1
    return count

def main(hi: int):
    q = 1
    record = 0
    while q <= hi:
        count = countHailstone(q)
        if count >= record:
            record = count
            print(str(q) + " took " + str(count) + " steps.")
        q += 1

main(10000)