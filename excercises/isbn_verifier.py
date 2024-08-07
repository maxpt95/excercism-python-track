def is_valid(isbn: str) -> bool:
    """Determine the validity of an ISBN-10 code.

    A valid ISBN-10 confirms the following formula:
    (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    """
    isbn = isbn.replace("-", "")
    isbn_len = len(isbn)
    if isbn_len != 10:
        return False

    isbn_sum = 0
    for i, char in enumerate(isbn):
        # A valid ISBN-10 can only contain a non digit in it's last character and has to be an X
        if char.isnumeric():
            digit = int(char)
        elif char == "X" and i == isbn_len - 1:
            digit = 10
        else:
            return False

        isbn_sum += digit * (10 - i)

    return isbn_sum % 11 == 0
