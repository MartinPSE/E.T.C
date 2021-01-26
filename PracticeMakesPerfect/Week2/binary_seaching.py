finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequentail(target, array):
    current_min = 0
    current_max = len(array) - 1
    mid_num = ( current_max + current_min ) // 2
    while current_min <= current_max:
        if array[mid_num] == target:
            return print(True)
        elif array[mid_num] < target:
            current_min = mid_num + 1
        elif array[mid_num] > target:
            current_max = mid_num - 1
        mid_num = ( current_max + current_min ) // 2

    return print(False)


is_existing_target_number_sequentail(finding_target, finding_numbers)
