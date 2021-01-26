# k일 이후 밀가루 수입
# 향후 날짜 / 수량 /// 최소한의 횟수로 밀가루 공급
import heapq

ramen_stock = 4  # 현재 공장에 남아있는 밀가루 수량
supply_dates = [4, 10, 15]  # 밀가루 공급 일정
supply_supplies = [20, 5, 10]  # 해당 시점에 공급 가능한 밀가루 수량
supply_recover_k = 30  # 공장으로 공급받을 수 있는 시점 k


# 현재 재고가 바닥나는 시점 이전까지 받을 수 있는
# 라면 중 제일 많은 라면을 받는게 목표입니다.

# 제일 많은 -? 정렬?
# 1. 현재 재고의 상태에 따라 최곳값을 받아야 된다. (동적으로 변경되는 상태)
# 2. 제일 많은 값만 가져가면 된다.
# - Data 를 넣을때마다 최댓값을 동적으로 변경시키며,
# - 최소/ 최댓값을 바로 꺼낼 수 있는 자료구조.
# heap !!
# ramen_stock > k 보다 커야해

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    current_day_index = 0  # dates에 index
    max_heap = []  # 현재 공급량이 떨어지지 않는 한에서, supplies 를 해줘야해

    while stock < k:
        # date를 기준으로 반복 -> 지금 현재 stock이 0 이 되버리면 안됨.
        for date_index in range(current_day_index, len(dates)):
            print(date_index , dates[date_index], stock, supplies[date_index])
            if dates[date_index] <= stock:  # 현재 stock 4 / 요일이 10 (X)
                heapq.heappush(max_heap, -supplies[date_index])
            else:
                current_day_index = date_index
                break

        answer += 1

        stock += -heapq.heappop(max_heap)
        print("stock is", stock)
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
