# An Armstrong number is a number that is the sum of its own digits
# each raised to the power of the number of digits.

# For example:

# # 9 is an Armstrong number, because 9 = 9^1 = 9
# # 10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
# # 153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# # 154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
# Write some code to determine whether a number is an Armstrong number.


def is_armstrong_number(number: int) -> bool:
    """Checks if the number given is an armstrong number

    :param number: int - possible armstrong number.
    :return: bool - true if armstrong number.
    """
    number_str = str(number)
    return number == sum(int(digit) ** len(number_str) for digit in number_str)


if __name__ == "__main__":
    print(is_armstrong_number(153))
