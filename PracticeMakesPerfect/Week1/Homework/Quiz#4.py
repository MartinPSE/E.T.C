# string 이다 조심해라!!

input = "011110"

def count_all_to_zero_or_one(number):
    count_all_to_zero = 0
    count_all_to_one = 0
    leng = len(number)
    if number[0] == '0':
        count_all_to_one += 1
    elif number[0] == '1':
        count_all_to_zero += 1

    for i in range(leng-1):  # 0
        if number[i] != number[i+1]:
            if number[i+1] == '1':
                count_all_to_zero += 1
            elif number[i+1] == '0':
                count_all_to_one += 1

    return min(count_all_to_zero, count_all_to_one)


result = count_all_to_zero_or_one(input)
print(result)
print("hihihi")


