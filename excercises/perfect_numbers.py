import math


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if type(number) is not int or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    # Get all the factors of a number
    factors = set((i, number / i) for i in range(1, math.ceil(math.sqrt(number))) if number % i == 0)
    # The aliquout sum ofa number is the sum of all the factors of the number except for itself
    aliquot = sum(first + second for first, second in factors) - number

    if number == aliquot:
        return "perfect"
    elif number < aliquot:
        return "abundant"
    elif number > aliquot:
        return "deficient"
