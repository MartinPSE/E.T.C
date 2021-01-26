# 집합을 이용하자!
# 집합 - > 중복을 허용하지 않는 자료형.
# a = set([array...])
# 이분탐색은 절대적으로 효율적인 구조가 아니다.


menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "덤블링"]


# O(N) + O(M) = O ( M + N )

def is_available_to_order(menus, orders):
    menus_set = set(menus)  # O(N) - > set 화
    for order in orders:
        if order not in menus_set:  # O(1) * M = O(M)
            return False

    return True


print(is_available_to_order(menus, orders))