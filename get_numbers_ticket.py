import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1 or max > 1000 or min > max or quantity < 1:
        return []
    if quantity > max - min + 1:
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
