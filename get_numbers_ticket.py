import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    "checking parameters for compliance with constraints"
    if min < 1 or max > 1000 or not (min <= quantity <= max) or min > max:
        return []
    "generation of unique random numbers"
    numbers = random.sample(range(min, max + 1), quantity)
    "sorting the list of numbers in ascending order"
    return sorted(numbers)
