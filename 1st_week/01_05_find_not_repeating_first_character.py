def find_not_repeating_first_character(string):
    alphabet_array = [0] * 26
    not_repeating_alphabet_list = []
    for char in string:
        alphabet_array[ord(char) - ord('a')] += 1

    for index in range(len(alphabet_array)):
        if alphabet_array[index] == 1:
            not_repeating_alphabet_list.append(chr(index + ord('a')))

    if len(not_repeating_alphabet_list) < 1:
        return "_"

    for char in string:
        if char in not_repeating_alphabet_list:
            return char


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))