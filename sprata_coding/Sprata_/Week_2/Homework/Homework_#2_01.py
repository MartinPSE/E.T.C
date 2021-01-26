# 배달의 민족 가능 여부

menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "덤블링"]

# O(N*logN) # O(M *logN)
# O( (M+N) * logN )
# 즉 비효율적이다.

def is_available_to_order(menus, orders):
    menus.sort()          # 정렬의 시간복잡도는 배열의 길이를 N 이라고 한다면,
                          # 0(N*logN)

    for order in orders:  # string  도 그냥 뽑기! # O(M *  logN)

        if not is_existing_target_number_binary(order, menus):  # O(logN)
            return False

    return True




def is_existing_target_number_binary(target, array):

    current_min = 0
    current_max = len(array) - 1  # index 는 0 부터 시작이잖아, you know ?
    current_guess = (current_min + current_max) // 2  # Up, Down 시작 숫자.   '//'쓰면 나머지 없어진다.


    while current_min <= current_max:  # 최소값이 최대값이랑 같아질때까지.

        if array[current_guess] == target:  # 50 !! -> 맞으면 바로 추출   ex ) 39생각한숫자 ->>> 50!!

            return True
        elif array[current_guess] < target:  # 51 ~ 100 Up !!!      Up 이야
            current_min = current_guess + 1
        else:                                # 1 ~ 49 Down!!        Down 이야!
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2

    return False

print(is_available_to_order(menus, orders))