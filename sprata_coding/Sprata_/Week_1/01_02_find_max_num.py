input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]           # 연산 1번
    for num in array:            # array
        if num > max_num:        # 비교 연산 1번
            max_num=num          # 대입 연산 1번 
            
    return max_num


result= find_max_num(input)
print(result)
