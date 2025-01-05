input = 20

# 이전의 수와 이전 이전의 수의 합이 n이어야 한다.
def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765