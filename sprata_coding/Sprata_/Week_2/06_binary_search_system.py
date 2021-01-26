# UP,DOWN 게임 느낌으로.

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# 1 ~ 100
#   50 시작
#  UP ? 51 - 100

#  Down ? 1 - 49

# O(log N)의 시간복잡도를 갖는다.


def is_existing_target_number_binary(target, array):

    current_min = 0
    current_max = len(array) - 1  # index 는 0 부터 시작이잖아, you know ?
    current_guess = (current_min + current_max) // 2  # Up, Down 시작 숫자.   '//'쓰면 나머지 없어진다.
    find_count = 0

    while current_min <= current_max:  # 최소값이 최대값이랑 같아질때까지.
        find_count += 1
        if array[current_guess] == target:  # 50 !! -> 맞으면 바로 추출   ex ) 39생각한숫자 ->>> 50!!
            print(find_count)
            return True
        elif array[current_guess] < target:  # 51 ~ 100 Up !!!      Up 이야
            current_min = current_guess + 1
        else:                                # 1 ~ 49 Down!!        Down 이야!
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
