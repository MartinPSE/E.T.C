# 쓱 최대로 할인 적용하기 / 문제를 잘 못 이해했어.
# 내 쿠폰있는 만큼만 쓸 수 있는거야

shop_prices = [30000, 2000, 1500000]

user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    prices_index = 0
    coupons_index = 0
    get_max_prices = 0
    while prices_index < len(prices) and coupons_index < len(coupons):
        get_max_prices += prices[prices_index] * (100 - coupons[coupons_index]) / 100

        coupons_index += 1
        prices_index += 1

    while prices_index < len(prices):
        get_max_prices += prices[prices_index]
        prices_index += 1
    return get_max_prices


print(get_max_discounted_price(shop_prices, user_coupons))
