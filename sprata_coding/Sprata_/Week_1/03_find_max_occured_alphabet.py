input = "hello my name is sparta"



def find_max_occurred_alphabet(string):

    alphabet_array = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"
                      "s","t","u","v","w","x","y","z"]
       # -> 26 개의 공간
    max_occurrence = 0    # -> 1개
    max_alphabet = alphabet_array[0]   # -> 1개

    for alphabet in alphabet_array :      # 26만큼 반복
        occurrence = 0                    # -> 1개
        for char in string:               # for 문 돌고
            if char == alphabet:          # 비교 연산 1번
                occurrence += 1           # 대입 연산 1번

        if occurrence > max_occurrence:   # 비교 연산 1번
            max_occurrence = occurrence   # 대입 연산 1번
            max_alphabet = alphabet       # 대입 연산 1번



    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)

 # 52 N + 104 만큼의 '시간 복잡도'
 # 52 N 만큼.
