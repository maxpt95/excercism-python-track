def leap_year(year: int) -> bool:
    """Checks year is a leap year

    :param year: int.
    :return: bool - true if year is a leap year.
    """
    # A year is leap year when divisible by 4. Unless is divisible by 100,
    # in which case it also needs to be divisible by 400
    if year % 100 == 0:
        return year % 400 == 0

    return year % 4 == 0


if __name__ == "__main__":
    print(leap_year(1997))
    print(leap_year(1900))
    print(leap_year(2000))
    print(leap_year(2024))
