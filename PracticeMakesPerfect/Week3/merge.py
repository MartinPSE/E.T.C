array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


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


print(merge(array_a, array_b))
