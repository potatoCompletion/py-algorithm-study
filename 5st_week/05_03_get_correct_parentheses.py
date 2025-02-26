from collections import deque

balanced_parentheses_string = "()))((()"
# ()(())
# balanced_parentheses_string = ")("

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.


def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == '':
        return ''

    u = ''
    v = ''
    count = 0

    for i in range(0, len(balanced_parentheses_string)):
        now_char = balanced_parentheses_string[i]

        if balanced_parentheses_string[i] == '(':
            count += 1
            u += now_char
        else:
            count -= 1
            u += now_char

        if count == 0:
            start_index = i + 1

            if validRight(u):
                u += get_correct_parentheses(balanced_parentheses_string[start_index:])
                return u
            else:
                temp_u = '('
                temp_u += get_correct_parentheses(balanced_parentheses_string[start_index:])
                temp_u += ')'
                u = u[1:-1]
                temp_char = u.replace('(', 'a').replace(')', 'b')
                u = temp_char.replace('a', ')').replace('b', '(')
                u = temp_u + u
                return u

    return u

def validRight(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))