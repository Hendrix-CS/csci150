def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

def hailstoneSteps(n: int) -> int:
    count = 0
    while n > 1:
        n = hailstone(n)
        count += 1
    return count

def countStepsUpTo(hi: int):
    n = 1
    while n <= hi:
        print (str(n) + " " + str(hailstoneSteps(n)))
        n += 1

def findStepRecords(hi: int):
    n = 1
    record = 0
    while n <= hi:
        steps = hailstoneSteps(n)
        if steps > record:
            record = steps
            print (str(n) + " " + str(record))
        n += 1

def main():
    findStepRecords(100000)

main()
