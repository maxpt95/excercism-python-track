#Calculate the number of grains of wheat on a chessboard given 
#that the number on each square doubles.
#There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).
CHESSBOARD_SQUARES = 64
GRAINS_IN_FIRST_SQUARE = 1

def square(number: int) -> int:
    """Calculates the number of grains on a given squre

    :param number: int - the square number.
    :return: int - grain number.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    elif number == 1:
        return 1
    # return 2**(number - 1) * GRAINS_IN_FIRST_SQUARE
    return 1 << (number - 1)

def total() -> int:
    """The total number of grain on a chessboard

    :return: int - number of grain on the chessboard.
    """
    grain = 0
    for square_num in range(1, CHESSBOARD_SQUARES + 1):
        grain += square(square_num)
        
    return grain

if __name__ == "__main__":
    print(square(1))
    print(square(2))
    print(square(4))
    print(total())