import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 재고로 버틸 수 있는 날짜를 계산한다.
# (1)재고로 버틸 수 있는 날짜 이전의 공급일자 중에, (2)가장 많은 수량의 물자를 공급받는다.

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    heap = []
    last_added_index = 0

    while stock < k:
        while last_added_index < len(dates) and dates[last_added_index] <= stock:
            heapq.heappush(heap, supplies[last_added_index] * -1)
            last_added_index += 1

        stock += heapq.heappop(heap) * -1
        answer += 1

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))


# import heapq
#
# ramen_stock = 4
# supply_dates = [4, 10, 15]
# supply_supplies = [20, 5, 10]
# supply_recover_k = 30
#
#
# def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
#     answer = 0
#     last_added_date_index = 0
#     max_heap = []
#
#     while stock <= k:
#         while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
#             heapq.heappush(max_heap, -supplies[last_added_date_index])
#             last_added_date_index += 1
#
#         answer += 1
#         heappop = heapq.heappop(max_heap)
#         stock += -heappop
#
#     return answer
#
#
# print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
# print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
# print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
# print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))