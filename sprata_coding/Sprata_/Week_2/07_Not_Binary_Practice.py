finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]
finding_numbers2 = sorted(finding_numbers)
print(finding_numbers2)


def is_existing_or_not(target, number):
    count_min = 0
    count_max = len(finding_numbers) - 1
    count_guess = (count_min + count_max) // 2
    count_count = 0
    while count_min <= count_max:
        count_guess += 1
        count_count += 1
        if finding_numbers2[count_guess] == target:
            print(count_count)
            return True
        elif count_guess < target:
            count_min = count_guess + 1
        else:
            count_max = count_guess - 1
        count_guess = (count_min + count_max) // 2
    return False


result = is_existing_or_not(finding_target, finding_numbers)
print(result)


