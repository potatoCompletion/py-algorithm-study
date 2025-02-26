import heapq

input = "abcabcabcabcdededededede"

# 1개부터 문자열의 길이 // 2만큼 차례대로 잘라서 검사
# AAAAZ = 4AZ

def string_compression(string):
    duplicate_count = 1
    prev_string = ''
    result = ''
    min_heap = []

    for i in range(1, len(string) // 2 + 1):
        for j in range(0, len(string) + 1, i):
            if j + i > len(string):
                result = append_string(result, duplicate_count, prev_string) + string[j:]
                prev_string = ''
                duplicate_count = 1
                break

            now_string = string[j:j + i]
            if prev_string == now_string:
                duplicate_count += 1
            else:
                result = append_string(result, duplicate_count, prev_string)
                prev_string = now_string
                duplicate_count = 1

        heapq.heappush(min_heap, len(result))
        result = ''

    return heapq.heappop(min_heap)

def append_string(result, duplicate_count, string):
    if duplicate_count == 1:
        return result + string
    else:
        return result + str(duplicate_count) + string


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))