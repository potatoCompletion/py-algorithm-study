from itertools import combinations

# 하나씩 잘라보고 합이 맞으면 +
# 맞지 않다면 부족한 만큼의 수가 다른쪽 배열에 있으면 옮겨서 +

# -1, -2,| 2, 1  6만큼 부족
#  -1 | -2, 2, 1 2만큼 부족
#  -1 -2 2 | 1  2만큼 부족

def solution(arr):
    answer = 0
    comb_array = []
    for i in range(len(arr)):
        comb_array.append(i)

    for i in range(1, len(arr)):
        arr_a, arr_b = arr[i:], arr[:i]
        a_sum, b_sum = 0, 0
        for a_num in arr_a:
            a_sum += a_num
        for b_num in arr_b:
            b_sum += b_num
        if a_sum == b_sum:
            answer += 1

    comb_list = list(combinations(comb_array, 2))

    for a, b in comb_list:
        temp_array = arr.copy()
        temp_array[a], temp_array[b] = temp_array[b], temp_array[a]

        for i in range(1, len(arr)):
            arr_a, arr_b = temp_array[i:], temp_array[:i]
            a_sum, b_sum = 0, 0
            for a_num in arr_a:
                a_sum += a_num
            for b_num in arr_b:
                b_sum += b_num
            if a_sum == b_sum:
                answer += 1

    return answer

print(solution([-1, -2, 2, 1]))