# 주어진 값 이하의 소수 찾기

# 우선 2를 제외한 짝수는 소수가 될 수 없다.
# 3부터 시작해서 홀수의 값으로 나머지 연산을 실행한 후, 0이면 소수가 아니다.
# 값의 1/2을 초과하는 값은 계산할 필요가 없다.

input = 20


def find_prime_list_under_number(number):

    prime_list = []
    for target_num in range(2, number + 1): # 파이썬에서 for - range(n, m)는 m - 1 까지 반복한다. 따라서 + 1을 해줘야 함.
         for compare_num in prime_list:
             if compare_num * compare_num <= target_num and target_num % compare_num == 0:
                 break
         else:
            prime_list.append(target_num)

    return prime_list

result = find_prime_list_under_number(input)
print(result)