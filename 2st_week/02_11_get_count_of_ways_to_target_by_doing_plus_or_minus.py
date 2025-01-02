# 더하거나 빼서 주어진 target_number의 값이 되는 경우의 수 구하기

# 어떻게 풀지 고민하다가 못푸는 경우가 있다. 그러므로 쉬운 예제를 만들어서 생각해보자

numbers = [1,1,1,1,1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    result = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index >= len(array):
            if current_sum == target_number:
                result.append(current_sum)
            return

        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)
    return len(result)

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!