import random
from typing import *


def int_input(prompt: str) -> int:
    value = input(prompt)
    while not value.isdigit():
        print(f"{value} is not an integer. Please try again.")
        value = input(prompt)
    return int(value)


def check(a: int, b: int, correct: List[str], incorrect: List[str]):
    problem = f"{a} + {b}"
    answer = int_input(f"{problem} = ")
    if a + b == answer:
        print("Correct!")
        correct.append(problem)
    else:
        print(f"Sorry, the correct answer is {a + b}.")
        print("Try again later - I know you can do it!")
        incorrect.append(problem)


def make_problem(low: int, high: int) -> Tuple[int,int]:
    # Avoid repeats
    a = random.randint(low, high)
    b = random.randint(low, high)
    return a, b


def main():
    target = int_input("How many correct answers is the goal? ")
    right_answers = []
    incorrect = []
    while len(right_answers) < target:
        a, b = make_problem(1, 12)
        check(a, b, right_answers, incorrect)

    print("You got the following problems correct:")
    print(right_answers)
    print()
    print("You should study the following problems, which had wrong answers:")
    print(incorrect)


main()
