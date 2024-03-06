def steps(number: int) -> int:
    """Calculates the number of steps to prove Collatz Conjecture

    :param number: int.
    :return: int - number of steps.
    """
    if number <= 0 or not isinstance(number, int):
        raise ValueError("Only positive integers are allowed")

    number_cc = number
    # Calculate next step until Collatz Conjecture number is 1
    steps_count = 0
    while number_cc != 1:
        steps_count += 1
        if number_cc % 2 == 0:
            number_cc /= 2
        else:
            number_cc = number_cc * 3 + 1

    return steps_count


if __name__ == "__main__":
    print(steps(12))
