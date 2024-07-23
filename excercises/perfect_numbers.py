import math
from typing import Set, Tuple


def get_factors(number: int) -> Set[Tuple]:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: Set[Tuple] a set containing all factor paris use in the number division
    """
    return set((i, number / i) for i in range(1, math.ceil(math.sqrt(number))) if number % i == 0)


def aliquot_sum(number: int) -> int:
    """Performs an aliquot sum on the number given"""
    factors = get_factors(number)
    return sum(first + second for first, second in factors) - number


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if type(number) is not int or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot = aliquot_sum(number)
    if number == aliquot:
        clasification = "perfect"
    elif number < aliquot:
        clasification = "abundant"
    elif number > aliquot:
        clasification = "deficient"

    return clasification
