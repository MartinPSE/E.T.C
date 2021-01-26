input = [3, 5, 6, 1, 2, 4]


# 시간 복잡도 O(N**2)
def find_max_num(array):
    for i in input:  # 3
        for j in input:  # 3, 5, 6 , 1, 2, 4
            if i < j:
                print(i, 'i')
                print(j, 'j')
                break
        else:
            return i



result = find_max_num(input)
print(result)
