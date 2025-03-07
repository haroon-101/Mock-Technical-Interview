from string import punctuation
import requests


def remove_punctuation(text: str) -> str:
    final_text = "".join(
        [letter for letter in text if letter not in punctuation])
    return final_text


def palindrome_check(text: str) -> bool:
    midpoint = len(text) // 2
    if not text:
        return True
    for i in range(len(text[:midpoint])):
        if text[i].lower() != text[-(i + 1)].lower():
            return False
    return True


def palindrome_check_list(words: list[str]) -> list[str]:
    passes = []
    for word in words:
        if palindrome_check(remove_punctuation(word)):
            passes.append(word)

    return passes


def get_word_from_dictionary(word: str) -> list[dict]:
    ...


def main():
    words = ["Racecar!", "hah", "haroon", "chris"]
    final_text = remove_punctuation(words)
    print(palindrome_check_list(final_text))


if __name__ == "__main__":
    main()
