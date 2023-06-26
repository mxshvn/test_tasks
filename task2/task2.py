import string


def replace_vowels_and_consonants(word: str) -> str:
    alphabet = list(string.ascii_lowercase)
    consonants = (
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
        'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
    )
    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ''

    for letter in word:
        if letter in vowels:
            letter_index = alphabet.index(letter)
            new_letter_index = letter_index - 1
            while alphabet[new_letter_index % len(alphabet)] not in consonants:
                new_letter_index -= 1
            result += alphabet[new_letter_index % len(alphabet)]
        elif letter in consonants:
            letter_index = alphabet.index(letter)
            new_letter_index = letter_index + 1
            while alphabet[new_letter_index % len(alphabet)] not in vowels:
                new_letter_index += 1
            result += alphabet[new_letter_index % len(alphabet)]
        else:
            result += letter

    return result


if __name__ == "__main__":
    case1 = "abcdtuvwxyz"
    print(replace_vowels_and_consonants(case1))
