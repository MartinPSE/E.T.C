# 더하거나 빼거나
# 모든 경우의 수를 다 찾아야한다.

# 모든 경우의 수.
# +5       +3       +1       -1        -3       -5
# +++++   ++++-   +++--    ++---     +----     -----

# N의 길이에 배열에서 더하거나 뺀 모든 경우의 수는
# N - 1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우 의 수를
# 추가하면 된다.

# [2,3]
# +2 +3 +1 / -1
# +2 -3 +1 / -1
# -2 +3 +1 / -1
# -2 -3 +1 / -1


numbers = [1, 1, 1, 1, 1]
target_number = 3

target_count = 0  # 변하지않는 프리미티브 단위 같은 경우는 / 파라미터로 넘기면 값을 복제해서 새로운 값을 생성해..


# 항상 변해버려 초기화 되버린다.
# 함수 바깥의 변수를 불러오려면 'global' 함수를 사용해야한다.


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):
        if current_sum == target:
            global target_count  # 함수 외부의 파라미터 불러오는 함수 -> global!
            target_count += 1

        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum + numbers[current_index]
    )

    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum - numbers[current_index]
    )


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0))
print(target_count)
