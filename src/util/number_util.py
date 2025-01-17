import random


def generate_numbers(n: int):
    numbers = ""
    for _ in range(n):
        i = random.randint(0, 9)
        numbers += str(i)
    return numbers
