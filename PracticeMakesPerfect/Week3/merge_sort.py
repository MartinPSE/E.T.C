array = [5, 3, 2, 1, 6, 8, 7, 4]
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = (0 + len(array)) // 2
    merge_left = merge_sort(array[:mid])
    merge_right = merge_sort(array[mid:])
    print('array: ', array)
    print('left_array : ', merge_left)
    print('right_array : ', merge_right)
    return merge(merge_sort(merge_left),merge_sort(merge_right))



def merge(array1, array2):
    result = []
    length_1 = len(array1)
    length_2 = len(array2)
    arr1_index = 0
    arr2_index = 0
    while arr1_index < length_1 and arr2_index < length_2:
        if array1[arr1_index] < array2[arr2_index]:
            result.append(array1[arr1_index])
            arr1_index += 1
        else:
            result.append(array2[arr2_index])
            arr2_index += 1

    if arr1_index == length_1:
        while arr2_index < length_2:
            result.append(array2[arr2_index])
            arr2_index +=1
    if arr2_index == length_2:
        while arr1_index < length_1:
            result.append(array1[arr1_index])
            arr1_index += 1




    return result


print(merge_sort(array))
