# 문자열 요약하기
# 아래 입력이 들어오게 된다면 a1/c3/d1/e3 과 같은 형태로 반환해야 함.
# 알파벳 관련 문제가 나오면 아스키 코드를 항상 생각하자

def summarize_string(input_str):
    alphabet_array = [0] * 26
    for char in input_str:
        alphabet_array[ord(char) - 97] += 1

    result_string = ""
    for num in range(0, len(alphabet_array)):
        if alphabet_array[num] == 0:
            continue
        result_string += chr(num + 97) + str(alphabet_array[num]) + "/"

    return result_string[:-1]

input_str = "acccdeee"

print(summarize_string(input_str))