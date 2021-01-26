# 딱히 내용 없으면 귀납적 추론을 해보자!
# 최소한의 자리쌍은 2자리 부터 시작.
# 2, 3, 4, 5, ..... ,i


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


seat_count = 9
vip_seat_array = [4, 7]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_way = 1  # 모두 앉아있는거 1개.
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        current_way = fibo_dynamic_programming(fixed_seat_index - current_index, memo)

        all_way *= current_way
        current_index = fixed_seat_index + 1  # VIP석 이전까지 완료.

    current_way = fibo_dynamic_programming(total_count - current_index, memo)
    all_way *= current_way
    return all_way



# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
