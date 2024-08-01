"""Calculate the points scored in a single toss of a Darts game.

If the dart lands outside the target, player earns no points (0 points).
If the dart lands in the outer circle of the target, player earns 1 point.
If the dart lands in the middle circle of the target, player earns 5 points.
If the dart lands in the inner circle of the target, player earns 10 points.
"""

import math


def score(x: int, y: int) -> int:
    """Calculate the points scored in a single toss of a Darts game.
    :param x, y: int - cartesian coordinates.
    :return: int - dart shot score.
    """
    h = math.sqrt(x**2 + y**2)
    if h > 10:
        return 0
    if h > 5:
        return 1
    if h > 1:
        return 5

    return 10
