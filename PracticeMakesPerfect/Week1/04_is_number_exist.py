input = [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
    count = False
    if number in array:
        count = True

    return count

result = is_number_exist(5, input)
print(result)