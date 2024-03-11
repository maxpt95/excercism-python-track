"""Determine if a triangle is equilateral, isosceles, or scalene."""

from typing import List


def is_triangle(sides: List[float]) -> bool:
    """Checks if a triangle can exists out of a list of sides measurements"""

    return (
        len(sides) == 3
        and sides.count(0) == 0
        and sides[0] + sides[1] >= sides[2]
        and sides[1] + sides[2] >= sides[0]
        and sides[2] + sides[0] >= sides[1]
    )


def equilateral(sides: List[float]) -> bool:
    """Checks if sides can form an equilateral triangle"""
    if not is_triangle(sides):
        return False

    # An equilateral triangle has all three sides the same length.
    return sides[0] == sides[1] and sides[1] == sides[2] and sides[2] == sides[0]


def isosceles(sides: List[float]) -> bool:
    """Checks if sides can form an isosceles triangle"""
    if not is_triangle(sides):
        return False

    # An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]


def scalene(sides: List[float]) -> bool:
    """Checks if sides can form an scalene triangle"""

    if not is_triangle(sides):
        return False

    # An scalene triangle has all sides of different lengths.
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]
