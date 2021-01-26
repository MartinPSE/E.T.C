# 문자열 뒤집기

input="011110"

# 011110
# 모두 0으로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_zero
# 0 -> 1로 문자열이 전환되는 순간 += 1


# 모두 1로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_one
# 1 -> 0ㄹ 문자열이 전환되는 순간 += 1

# 1) 뒤집어질때, 즉 0에서 1 혹은 1에서 0으로 바뀔 때
# 2) 첫 번째 원소가 0인지 1인지에 따라서 += 1
# 3)


def find_count_to_turn_out_to_all_zero_all_one(string):
    count_to_all_zero=0
    count_to_all_one=0
    if string [0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1
    for i in range(len(string) - 1):
        if string[i] != string [i+1]:
            if string[i+1]== '0':
                count_to_all_one += 1
            if string[i+1]== '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result=find_count_to_turn_out_to_all_zero_all_one(input)
print(result)