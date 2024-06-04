# Your task is to convert a number into its corresponding raindrop sounds.

# If a given number:
# is divisible by 3, add "Pling" to the result.
# is divisible by 5, add "Plang" to the result.
# is divisible by 7, add "Plong" to the result.
# is not divisible by 3, 5, or 7, the result should be the number as a string.


def convert(number: int) -> str:
    RAINDROPS = (3, "i"), (5, "a"), (7, "o")
    return "".join(f"Pl{v}ng" for d, v in RAINDROPS if not number % d) or str(number)


if __name__ == "__main__":
    print(convert(28))
    print(convert(30))
    print(convert(34))
