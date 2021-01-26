input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:  # array 의 길이만큼 아래 연산 실행
        print(num, "내가 num")
        for compare_num in array:  # array 의 길이만큼 아래 연산 실행
            if num < compare_num:  # 비교 연산 1번 실행

                print(compare_num, "내가 compare")
                break
        else:
            return num


result = find_max_num(input)

