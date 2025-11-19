# Recall factorial: n! = product of all numbers from 1 up to n.
#  e.g. 5! = 1 * 2 * 3 * 4 * 5 = 120

# We could compute this with e.g. a loop:

def factorial(n: int) -> int:
    result: int = 1
    for i in range(1, n+1):
        result *= i

    return result

# Notice that
#
#   n! = n * (n-1) * (n-2) * ... * 1
#      = n * ((n-1) * (n-2) * ... * 1)
#      = n * (n-1)!
#
#   also, 1! = 1  (or 0! = 1)
#
# We could take this as the *definition* of factorial:
#
#   1! = 1
#   n! = n * (n-1)!

def factorial2(n: int) -> int:
    if n == 1:      # 1! = 1
        return 1
    else:
        return n * factorial2(n-1)


# "Recursion" = defining a function in terms of itself. Put another way, writing a function which calls itself.
#
#  Need 2 things for this to make sense:
#
#    - There must be a "base case", i.e. a simple case in which the function simply returns the answer
#      without calling itself again
#    - Every time the function calls itself, the input must get "smaller" (i.e. closer to the base case).


# Example: adding up numbers in a list

# [1, 4, 6, 9, 2]

def list_sum(nums: list[int]) -> int:
    # if nums == [0]:
    #     return 0
    # if len(nums) == 1:
    #     return nums[0]
    if len(nums) == 0:
        return 0
    else:
        # The first number + sum of all the rest
        return nums[0] + list_sum(nums[1:])





# Example: multiplying all the numbers in a list
# e.g. list_product([2,3,5]) = 30
def list_product(nums: list[int]) -> int:
    # 1. Base case
    if nums == []:
        return 1
    else:
        # Leap of faith: ASSUME any recursive calls will give us the
        # correct answer on the smaller input, then figure out what to do
        # to get the answer on the bigger input.

        rest_prod = list_product(nums[1:]) # ASSUME that rest_prod will be the correct product
                                           # of nums[1:].

        # To get the product of the entire list, just multiply by nums[0].
        whole_prod = nums[0] * rest_prod

        return whole_prod



