"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
LAYER_PREPARATION_TIME = 2


# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elpased_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elpased_bake_time


# TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers: int):
    """Calculation lasagna preparation time per number of layers

    :param number_of_layers: int - number of layers in the lasagana.
    :return: preparation time in minutes.
    """
    return number_of_layers * LAYER_PREPARATION_TIME


# TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate elpased cooking time.

    :param number_of_layers: int - umber of layers in the lasagana.
    :param elapsed_bake_time: int - elapsed baking time.
    :return: elpased cooking time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


if __name__ == "__main__":
    print(f"bake time remaining: {bake_time_remaining(30)}")
    print(f"preparation time in minutes: {preparation_time_in_minutes(2)}")
    print(f"elapsed time in minutes: {elapsed_time_in_minutes(3, 20)}")
