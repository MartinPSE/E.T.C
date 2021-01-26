# k일 이후 밀가루 수입
# 향후 날짜 / 수량 /// 최소한의 횟수로 밀가루 공급
import heapq

ramen_stock = 4  # 현재 공장에 남아있는 밀가루 수량
supply_dates = [4, 10, 15]  # 밀가루 공급 일정
supply_supplies = [20, 5, 10]  # 해당 시점에 공급 가능한 밀가루 수량
supply_recover_k = 30  # 공장으로 공급받을 수 있는 시점 k


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    count_answer = 0
    cur_index = 0
    max_heap = []
    while stock < k:
        for date_index in range(cur_index, len(dates)):
            if dates[date_index] <= stock:
                heapq.heappush(max_heap, -supplies[date_index])
            else:
                cur_index = date_index
                break

        count_answer += 1
        stock += -heapq.heappop(max_heap)
    return count_answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
