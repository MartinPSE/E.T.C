# 선택정렬
# 선택해서 정렬을 한다!
#  5 -> 4 -> 3-> 2 -> 1 비교 후 차례차례 옮기기


input = [4, 6, 2, 9, 1]


# O(N^2)  의 시간복잡도.

def selection_sort(array):
    n = len(array)
    for i in range(n - 1):  # i = 0 range 4
        min_index = i  # 0
        for j in range(n - i):  # j = 0 range 4
            if array[i + j] < array[min_index]:  # array[] < array[0]
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]
    print(input)


selection_sort(input)
