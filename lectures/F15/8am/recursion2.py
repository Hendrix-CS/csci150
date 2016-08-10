# More recursion

# Structure:
#   - Base case(s): know the answer
#   - Recursive case(s): solve a simpler problem + a bit of work

# "Leap of faith": trust your future self to implement recursive
#   calls correctly.

def fact(n):
    """Compute the factorial of n."""
    if n == 0:
        return 1
    else:
        # assume fact(n-1) will correctly compute (n-1)!
        # (even though I haven't finished writing it!)
        m = fact(n-1)
        return n * m

def sum(numbers):
    """Compute the sum of a list of numbers."""
    if numbers == []:
        return 0
    else:
#        rec_result = sum(numbers[1:])
#        return numbers[0] + rec_result

        return numbers[0] + sum(numbers[1:])

def reverse(string):
    """Reverse a string."""
    if string == "":
        return ""
    else:
        return reverse(string[1:]) + string[0]

def is_palindrome(string):
    """Test whether a string is a palindrome (the same
    forward and backward). Returns a boolean."""

    # Base case
    if string == "":
        return True
    else:
        rec_result = is_palindrome(string[1:-1])
        first_last_same = string[0] == string[-1]
        return rec_result and first_last_same
