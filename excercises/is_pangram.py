def is_pangram(sentence: str) -> bool:
    """Check whether a sentence is a pangram."""
    unique_letters = set()
    for char in sentence.lower():
        if char.isalpha():
            unique_letters.add(char)

    return len(unique_letters) >= 26
