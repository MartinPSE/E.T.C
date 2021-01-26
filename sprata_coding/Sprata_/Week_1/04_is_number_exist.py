input = [4, 5, 6, 1, 2, 3]

def is_number_exist(number, array):
    for element in array:          # array의 길이 만큼 연산 실행
        if number == element:      # 비교 연산 1번
           return True             # N * 1 = N ( 시간 복잡도 )
 
    return False

result = is_number_exist (9, input)
print(result)