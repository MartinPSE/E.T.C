input = "abacbade"


def find_not_repeating_character(string):
    alphabet_occurrancy = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        char_index = ord(char) - ord("a")  # 0
        alphabet_occurrancy[char_index] += 1  # 0

    for index in range(len(alphabet_occurrancy)):
        alphabet_occurrence = alphabet_occurrancy[index]
        if alphabet_occurrence == 1:
            return chr(index + ord("a"))

    return '_'

result = find_not_repeating_character(input)
print(result)
