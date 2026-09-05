import random


def generate_list(size):
    return [random.randint(0, 1_000_000) for _ in range(size)]
