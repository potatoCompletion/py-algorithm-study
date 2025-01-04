# deque 사용해야 한다.
from collections import deque

prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    answer = []
    queue = deque(prices)

    while queue:
        target = queue.popleft()
        not_fall_period = 0
        for price in queue:
            if target > price:
                not_fall_period += 1
                break
            else:
                not_fall_period += 1

        answer.append(not_fall_period)

    return answer


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))