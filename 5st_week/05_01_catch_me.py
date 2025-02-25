from collections import deque

c = 11
b = 2
dict = {}

# cony의 이동 = c, c + 1, c + 3 ...
# brown의 이동 = b - 1, b + 1, b * 2
# 0 <= p <= 200,000
# brown의 모든 경우의 수를 구하고 저장, 그 중 cony의 위치와 일치하는 것이 있는지 확인

def catch_me(cony_loc, brown_loc):
    queue = deque()
    queue.append(brown_loc)
    dict[0] = queue
    time = 0
    while cony_loc <= 200000:
        cony_loc = cony_loc + time

        if valid_cony_loc_and_calculate_next_brown_loc(time, cony_loc):
            return time

        time = time + 1

    return -1

def valid_cony_loc_and_calculate_next_brown_loc(time, cony_loc):
    queue = dict[time] # 현재 time

    # 현재 time 키 값이 가지는 queue에 cony_loc이 들어있다면 만났다
    if cony_loc in queue:
        return True

    new_set = set() # 중복 데이터 거르기 위한 set

    while queue:
        target_num = queue.popleft()

        if 0 <= target_num - 1 <= 200000:
            new_set.add(target_num - 1)
        if 0 <= target_num + 1 <= 200000:
            new_set.add(target_num + 1)
        if 0 <= target_num * 2 <= 200000:
            new_set.add(target_num * 2)

    # set에 저장한 자료들을 모두 다음 count 인덱스에 queue로 저장
    new_queue = deque()
    for num in new_set:
        new_queue.append(num)
    dict[time + 1] = new_queue

    return False

print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))