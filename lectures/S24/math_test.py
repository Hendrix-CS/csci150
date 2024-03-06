import random
from typing import *


def int_input(prompt: str) -> int:
    value = input(prompt)
    while not value.isdigit():
        print(f"{value} is not an integer. Please try again.")
        value = input(prompt)
    return int(value)


def make_add_string(a: int, b: int) -> str:
    return f"{a} + {b}"


def check(a: int, b: int, correct: List[str], incorrect: List[str]):
    problem = make_add_string(a, b)
    answer = int_input(f"{problem} = ")
    if a + b == answer:
        print("Correct!")
        correct.append(problem)
    else:
        print(f"Sorry, the correct answer is {a + b}.")
        print("Try again later - I know you can do it!")
        incorrect.append(problem)


def is_repeated(a: int, b: int, previous_problems: List[str]) -> bool:
    prob_string = make_add_string(a, b)
    #for x in range(0, len(previous_problems), 1):
    #for x in range(0, len(previous_problems)):
    for x in range(len(previous_problems)):
        if prob_string == previous_problems[x]:
            return True
    return False


def is_repeated_2(a: int, b: int, previous_problems: List[str]) -> bool:
    prob_string = make_add_string(a, b)
    for x in previous_problems:
        if prob_string == x:
            return True
    return False


def make_problem(low: int, high: int, previous_problems: List[str]) -> Tuple[int, int]:
    a = random.randint(low, high)
    b = random.randint(low, high)
    while is_repeated(a, b, previous_problems):
        a = random.randint(low, high)
        b = random.randint(low, high)
    return a, b


def alt_make_problem(previous_problems: List[str],
                     problem_list: List[Tuple[int, int]]) -> Tuple[int, int]:
    a, b = problem_list[0]
    while is_repeated_2(a, b, previous_problems):
        problem_list = problem_list[1:]
        a, b = problem_list[0]
    return a, b


def main():
    problem_list = [(2, 3), (4, 5), (1, 7), (8, 2), (5, 3)]
    target = int_input("How many correct answers is the goal? ")
    right_answers = []
    incorrect = []
    while len(right_answers) < target:
        #a, b = make_problem(1, 12, right_answers)
        a, b = alt_make_problem(right_answers, problem_list)
        check(a, b, right_answers, incorrect)
        problem_list = problem_list[1:] + [problem_list[0]]

    print("You got the following problems correct:")
    print(right_answers)
    print()
    print("You should study the following problems, which had wrong answers:")
    print(incorrect)


main()
