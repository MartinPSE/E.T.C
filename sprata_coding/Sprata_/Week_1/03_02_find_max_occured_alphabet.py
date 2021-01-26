input = "good morning alphas! i'm martin! "



def find_max_value(string):
    alpha_array = [0] * 26        # 26개의 공간

    for char in string:           #
        if not char.isalpha():    #
            continue
        alpha_index = ord(char) - ord("a")  # 1개
        alpha_array[alpha_index] += 1  # 1개

    max_alpha = 0          # 1개
    max_alpha_index = 0    # 1개
    for index in range(len(alpha_array)):  #
        alphabet_occur = alpha_array[index]   # 연산
        if alphabet_occur > max_alpha:  # 비교 연산 1번
            max_alpha = alphabet_occur  # 대입 연산 1개
            max_alpha_index = index     # 대입 연산 1개

    return chr(max_alpha_index + ord('a'))


result = find_max_value(input)
print(result)




# 3N + 106
# 즉 3N 이야. 