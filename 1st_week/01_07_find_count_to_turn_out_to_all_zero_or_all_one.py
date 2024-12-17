# 모두 한 문자로 만드는 최소 횟수 구하기

# 붙어있는 문자는 하나로 간주해야 한다. ex) 0000 = 0



input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_or_one_array = [0] * 2
    now_number = string[0]
    for char in string:
        if char != now_number:
            zero_or_one_array[int(now_number)] += 1
            now_number = char

    zero_or_one_array[int(string[len(string) - 1])] += 1

    return min(zero_or_one_array[0], zero_or_one_array[1])


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)