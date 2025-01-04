# 올바른 괄호인지 판단
# 왼쪽부터 하나씩 빼가면서 열린 괄호 개수보다 닫힌 괄호 개수가 많아지면 올바르지 않은 괄호이다.

from collections import deque

def is_correct_parenthesis(string):
    stack = []

    for s in string:
        if s == "(":
            stack.append("(")
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    else:
        return True

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))