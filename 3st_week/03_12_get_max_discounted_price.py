# 최대 할인 받았을 때 낼 가격 반환하기
# 할인이 %이기 때문에 가격은 높을수록 할인액이 늘어난다. 할인도 마찬가지로 높을수록 좋다.
import math

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort()
    coupons.sort()
    price_sum = 0

    while prices:
        if not coupons:
            for i in range(len(prices)):
                price_sum += prices.pop()
        else:
            current_price = prices.pop()
            current_coupon = coupons.pop()
            price_sum += current_price * (100 - current_coupon) / 100

    return math.floor(price_sum)


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))