def is_isogram(string: str) -> bool:
    """Determine if a word or phrase is an isogram."""
    string = string.replace(" ", "").replace("-", "").lower()
    return len(string) == len(set(string))
