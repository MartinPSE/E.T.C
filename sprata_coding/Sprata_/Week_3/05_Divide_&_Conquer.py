# 분할 정복 / 병합 정렬

array = [5, 3, 2, 1, 6, 8, 7, 4]

# merge_sort -> N/2 * 2 -> N
#            -> N/4 * 4 -> N
#            -> ... 모든 단계에서 N 만큼의 시간복잡도를 갖는다.
# k 단계 : N ------> 1 이 된다!
# N/2^k = 1  ->       K -> log2N
# 따라서 O(log2N) * O(N) -> O(NlogN) 만큼의 시간이 걸린다.


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    return merge(merge_sort(left_array), merge_sort(right_array))


# merge -> O(N) 만큼 시간복잡도


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):  # O(N)
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1
    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))
