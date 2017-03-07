### 1 ###
def adjacent_bad(nums):
  for i in nums:
    if nums[i] % 2 == 0:
      if nums[i - 1] % 2 == 1 or nums[i + 2] % 2 == 1:
        return True
      else:
        return False

def adjacent(nums):
  for i in range(1,len(nums) - 1):
    if nums[i] % 2 == 0:
      if not (nums[i - 1] % 2 == 1 or nums[i + 1] % 2 == 1):
        return False

  return True



### 2 ###
t = "WHEREINTHEWORLDIS"
r = "CarmenSandiego"
p = t.find("R") * 4 - 1
f = r[-3:]
n = t[p:p + 2] + f + "N"
n.lower()



### 3 ###
def get_sum_bad():
    valid = False
    while not valid:
      value1 = input("Enter a number:")
      if value1.isdigit() or value1[0] == '-' and value1[1:].isdigit():
        valid = True
        value1 = int(value1)
      else:
        print("not a number, try again")

    valid = False
    while not valid:
      value2 = input("Enter another number:")
      if value2.isdigit() or value2[0] == '-' and value2[1:].isdigit():
        valid = True
        value2 = int(value2)
      else:
        print("not a number, try again")

    print("Sum: ", value1 + value2)

def input_integer(prompt):
    valid = False
    while not valid:
        value = input(prompt)
        if value.isdigit() or value[0] == '-' and value[1:].isdigit():
            valid = True
            value = int(value)
        else:
            print("not a number, try again")
    return value

def get_sum():
    value1 = input_integer("Enter a number: ")

    value2 = input_integer("Enter another number:")

    print("Sum: ", value1 + value2)


### 4 ###
def splaz(n):
    steps = 0
    while n != 1 and steps < 100:
        if n % 3 == 0:
            n = n / 3
        else:
            n = 2*n + 1
        steps += 1

    if n == 1:
        return steps
    else:
        return -1


### 5 ###
def isogram1(s):
  for c in s:
    if s.count(c) > 1:
      return False
  return True

def isogram2(s):
  for i in range(len(s)):
    if s.find(s[i], i+1) != -1:
      return False
  return True

def isogram3(s):
  for i in range(len(s)):
    for j in range(i+1,len(s)):
      if s[i] == s[j]:
        return False
  return True
