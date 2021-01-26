shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    max_sum = 0
    price_index = 0
    coupon_index = 0
    while price_index < len(prices) and coupon_index < len(coupons):
        max_sum += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1
    while price_index < len(prices):
        max_sum += prices[price_index]
        price_index += 1

    return max_sum



print(get_max_discounted_price(shop_prices, user_coupons))
