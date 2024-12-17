def find_max_occurred_alphabet(string):
    arr = [0] * 26
    for alphabet in string:
        if alphabet.isalpha():
            arr[ord(alphabet) - 97] += 1

    max_index = 0
    for number in range(len(arr) - 1):
        if arr[number] > arr[max_index]:
            max_index = number

    return chr(max_index + 97)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))