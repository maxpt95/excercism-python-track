"""Functions for calculating steps in exchaning currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculates value of an exchanged currency

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate the amount of money left from the budget

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate the summ of bills of the same denomination

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Calculate how many bills you can receive of a given denomination from an ammount of money

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return int(amount // denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """Calculate the leftover ammount that can't be returned

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    total_money_received = get_value_of_bills(
        denomination, get_number_of_bills(amount, denomination)
    )

    return amount - total_money_received


def exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """Calculates maximum value of the new currency after exchange rates and fees

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread = spread / 100
    ammount_money_after_fees = exchange_money(
        budget, exchange_rate + exchange_rate * spread
    )

    number_of_bills = get_number_of_bills(ammount_money_after_fees, denomination)

    return get_value_of_bills(denomination, number_of_bills)


if __name__ == "__main__":
    print(f"exchange money: {exchange_money(127.5, 1.2)}")
    print(f"get change: {get_change(127.5, 120)}")
    print(f"get value of bill: {get_value_of_bills(5, 128)}")
    print(f"get number of bills: {get_number_of_bills(127.5, 5)}")
    print(f"get leftove of bills: {get_leftover_of_bills(127.5, 20)}")
    print(
        f"exchangeable values 127.25 budget, 20 denomination bills: {exchangeable_value(100000, 10.61, 10, 1)}"
    )
    print(
        f"exchangeable values 127.25 budget, 5 denomination bills: {exchangeable_value(127.25, 1.20, 10, 5)}"
    )
