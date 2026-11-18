# Recall "n factorial":  n! = 1 * 2 * 3 * .... * n
# e.g.  5! = 1 * 2 * 3 * 4 * 5 = 120

# One way we could do this in Python is with a loop:

def fact_loop(n: int) -> int:
    prod = 1
    for k in range(1, n+1):
        prod *= k

    return prod

# But notice:
#
# 5! = 1 * 2 * 3 * 4 * 5 = (1 * 2 * 3 * 4) * 5 = 4! * 5
# in general,
#
# 0! = 1
# n! = (n-1)! * n
#
# The above two lines are actually a valid way to define factorial.
# Can we turn this two-line definition directly into Python code?

def fact(n: int) -> int:
    # "base case": must be some case where we can return the answer
    # without making any more recursive calls.
    if n == 0:
        return 1
    else:
        # Recursive case: function calls itself on a *smaller*/*simpler* input.
        #
        # Leap of faith: *assume* that the recursive call will return the correct answer.
        # Figure out how to take a correct answer for the subproblem + turn it
        # into a correct answer for the overall problem.
        return fact(n-1) * n


# Example: function to add up all the numbers in a list.
def list_sum(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    # elif len(nums) == 1:    # this base case is actually unnecessary
    #     return nums[0]
    else:
        # Remove the first item from the list + add up the remaining numbers.
        # Assume this gives us the correct sum of all items except the first.
        sum_rest = list_sum(nums[1:])

        # Sum of the entire list is then the first item plus the sum of the rest.
        return nums[0] + sum_rest

# To do list_prod we could do the same above, except return 1 in the base case and multiply instead of add
# in the recursive case.

# A function to return a reversed version of the input list.
# e.g.   reverse_list(['dog', 'cat', 'cow']) == ['cow', 'cat', 'dog']
def reverse_list(words: list[str]) -> list[str]:
    if len(words) == 0:
        return []
    else:
        # Make the list simpler + call reverse_list on it recursively
        reverse_rest = reverse_list(words[1:])

        # Now stick the first element on the end
        return reverse_rest + [words[0]]