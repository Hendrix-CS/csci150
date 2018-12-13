def logarithm(b: float, n: float) -> int:
    if (n < b):
        return 0
    else:
        return 1 + logarithm(b, n/b)

def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

def main():
    print(logarithm(2, 128) == 7)
    print(logarithm(2, 35)  == 5)
    print(logarithm(5, 125) == 3)
    print(logarithm(2, 1)   == 0)
    print(logarithm(2, 3)   == 1)
    print(logarithm(10, 19740983) == 7)
    print('----------------------')
    print(is_palindrome('kayak'))
    print(is_palindrome('kayyak'))
    print(is_palindrome(''))
    print(is_palindrome('a'))
    print(is_palindrome('aa'))
    print(not is_palindrome('ab'))
    print(not is_palindrome('bbbbbbcbbb'))
    print(not is_palindrome('myhelicopterisfullofeels'))
    print(is_palindrome('amanaplanacanalpanama'))

main()
