# 피보나치 느낌으로 변화한다.
# 좌석이 i 개 있어, 1, 2, 3, 4, 5, 6, ... i
# i 번째 i번 티켓을 가진 사람이 그대로 앉는 경우
# i-1 좌석들을 맘껏 배치할 수 있는 경우의 수


# i 번째 티켓을 가진 사람이 i-1 번째 앉는 경우 가능.
# but i-1번째 앉았던 사람은 i에 앉을 수 밖에 없어..... -> 가다보면 1번자리의 사람이 옮길수가 없거든!
#                       i-1 i(i-1사람)
# i-2 좌석들을 맘껏 배치할 수 있는 경우의 수.
# 즉  F (N) = N 명의 사람들을 좌석에 배치하는 방법은
#          = N-1 명의 사람들을 좌석에 배치하는 방법 + N-2 명의 사람들을 좌석에 배치하는 방법
#          = F(N-1) + F(N-2)

seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}


# 1. 만약 메모에 있으면 그 값을 반환하고
# 2. 없으면 그 수식대로 구한다.
# 3. 그리고 그 값을 메모에 기록한다.

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1  # 다 그대로 앉아있을떄 1개!
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        # 지금부터 VIP석 까지 반복
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)

        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1  # VIP석 이후부터 다시 VIP석 까지 반복
    # VIP석 이후 좌석들에 대한 조건// 그 이후는 VIP석 없으니//
    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
