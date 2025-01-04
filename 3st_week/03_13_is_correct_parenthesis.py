# 올바른 괄호인지 판단
# 왼쪽부터 하나씩 빼가면서 열린 괄호 개수보다 닫힌 괄호 개수가 많아지면 올바르지 않은 괄호이다.

from collections import deque

def is_correct_parenthesis(string):
    queue = deque()

    for s in string:
        queue.append(s)

    open_num = 0

    while queue:
        current_char = queue.popleft()
        if current_char == "(":
            open_num += 1
        else:
            open_num -= 1

        if open_num < 0:
            return False

    return open_num == 0


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))