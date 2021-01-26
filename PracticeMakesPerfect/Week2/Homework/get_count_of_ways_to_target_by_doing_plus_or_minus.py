numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    array_list = [0]
    for i in array:
        temp_list = []
        for j in array_list:
            temp_list.append(j+i)
            temp_list.append(j-i)
        array_list = temp_list
    answer = array_list.count(3)
    return answer

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))
