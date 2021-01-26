input = "hello my name is sparta"


# 일단 ASCII 코드를 바탕으로 Alphabet 을 저장해야지!

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array_index = ord(char) - ord('a')  # 문자 ---> ASCII : ord()
        alphabet_occurrence_array[alphabet_occurrence_array_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index  # 0

        max_alphabet = chr(97) + chr(max_alphabet_index)  # 아스키 ---> 실제문자 chr()

    return max_alphabet

print(find_alphabet_occurrence_array(input))







def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                      "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    max_occurrence = 0
    max_alphabet = alphabet_array[0]
    for alphabet in alphabet_array:  # 알파벳을 지정!
        occurrence = 0
        for char in string:  # string 안에 임의의 스트링 char
            if char == alphabet:  # char == alphabet ?
                occurrence += 1

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet

    return max_alphabet



print(find_max_occurred_alphabet(input))





