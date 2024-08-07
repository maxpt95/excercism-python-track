import math


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot = sum(i + number / i for i in range(1, math.ceil(math.sqrt(number))) if number % i == 0) - number
    # The aliquout sum ofa number is the sum of all the factors of the number except for itself

    if number == aliquot:
        return "perfect"
    if number < aliquot:
        return "abundant"

    return "deficient"
