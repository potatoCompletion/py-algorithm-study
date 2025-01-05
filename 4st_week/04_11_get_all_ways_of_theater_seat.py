seat_count = 9
vip_seat_array = [4, 7]
memo = {
    1: 1,
    2: 2
}

# vip 좌석은 고정, 나머지는 +- 1까지 움직일 수 있음. 자리는 1 ~ seat_count 까지
# 경우의 수를 모두 구해야 함

# 2 = 2
# 3 = 3
# 4 = 5
# 5 = 8

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    result = 1
    current_seat = 1

    for fixed_seat in fixed_seat_array:
        result *= fibonacci(fixed_seat - current_seat)
        current_seat = fixed_seat + 1
        print(result)

    print("last fibo = ", fibonacci(total_count + 1 - current_seat))
    result *= fibonacci(total_count + 1 - current_seat)

    return result

def fibonacci(n):
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

# def fibonacci(n):
#     if n in memo:
#         return memo[n]
#
#     nth_fibo = fibonacci(n - 1) + fibonacci(n - 2)
#     memo[n] = nth_fibo
#     return nth_fibo

# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))



# seat_count = 9
# vip_seat_array = [4, 7]
#
# # 예전에 만들었던 fibo_dynamic_programming 에서 가져오면 됩니다!
# memo = {
#     1: 1,  # 이 문제에서는 Fibo(1) = 1, Fibo(2) = 2 로 시작합니다!
#     2: 2
# }
#
#
# def fibo_dynamic_programming(n, fibo_memo):
#     if n in fibo_memo:
#         return fibo_memo[n]
#
#     nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
#     fibo_memo[n] = nth_fibo
#     return nth_fibo
#
#
# def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
#     all_ways = 1
#     current_index = 0
#     for fixed_seat in fixed_seat_array:
#         fixed_seat_index = fixed_seat - 1
#         count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
#         all_ways *= count_of_ways
#         current_index = fixed_seat_index + 1
#
#     print(total_count - current_index)
#     count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
#     all_ways *= count_of_ways
#     return all_ways
#
#
# # 12가 출력되어야 합니다!
# print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
#
# print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
# print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
# print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))