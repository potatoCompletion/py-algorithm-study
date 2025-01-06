# 코니와 브라운의 위치는 0 <= x <= 200,000 을 만족한다.
# 코니는 이전 이동 거리 +1 만큼 위치가 증가 (c, c + 1, c + 3, c + 6, c + 10 ...)  c = 1, (1, 2, 4, 7, 11) 즉, 이전 총 이동거리 + 1
# 브라운은 B - 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니는 범위를 벗어나면 게임이 종료된다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.

#모든 경우의 수를 구해야 함 (BFS)

from collections import deque

c = 11
b = 2

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, time))

    visited = [[] for _ in range(200001)]

    while cony_loc <= 200000:
        # cony part
        cony_loc += time

        if time in visited[cony_loc]:
            return time

        # brown part
        for i in range(len(queue)):
            current_loc, current_time = queue.popleft()
            new_time = time + 1
            visited[new_time] = []

            # B - 1
            new_loc = current_loc - 1
            if 0 <= new_loc <= 200000:
                queue.append((new_loc, new_time))
                visited[new_loc].append(new_time)

            # B + 1
            new_loc = current_loc + 1
            if 0 <= new_loc <= 200000:
                queue.append((new_loc, new_time))
                visited[new_loc].append(new_time)

            # 2 * B
            new_loc = current_loc * 2
            if 0 <= new_loc <= 200000:
                queue.append((new_loc, new_time))
                visited[new_loc].append(new_time)

        time += 1

    return time




print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))