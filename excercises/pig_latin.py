# Your task is to translate text from English to Pig Latin. The translation is defined using four rules,
# which look at the pattern of vowels and consonants at the beginning of a word.
# These rules look at each word's use of vowels and consonants.

VOWELS = "a", "i", "e", "o", "u"


def find_separator(text: str) -> int:
    """Find the first partition separator"""
    i_min = len(text) - 1
    separators = VOWELS + ("qu", "y")

    for s in separators:
        i = text.find(s)
        if i == 0 and s == "y":
            continue
        if i != -1 and i <= i_min:
            i_min = i
            separator = s

    return separator


def translate(text: str) -> str:
    """Translate text to Pig Latin"""
    words = text.split()
    tranlastion = ""
    for word in words:
        starts_with_vocals = word.startswith(VOWELS)

        if starts_with_vocals or text.startswith(("xr", "yt")):
            return text + "ay"

        separator = find_separator(word)
        word_partition = word.partition(separator)
        if separator == "qu":
            tranlastion += " " + "".join(word_partition[2] + word_partition[0] + word_partition[1] + "ay")
        else:
            tranlastion += " " + "".join(word_partition[1] + word_partition[2] + word_partition[0] + "ay")

    return tranlastion.strip()


if __name__ == "__main__":
    print(translate("quick fast run"))
