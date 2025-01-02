# 재귀함수 이용한 펠린드롬

input = "소주만병병만만주소"


def is_palindrome(string):
    n = len(string)

    if n <= 1:
        return True

    if string[0] != string[n - 1]:
        return False

    return is_palindrome(string[1:-1])


print(is_palindrome(input))