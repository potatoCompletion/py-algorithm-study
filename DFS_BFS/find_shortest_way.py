from collections import deque

# 1은 길, 0은 벽
maps = [
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1]
]

def find_shortest_way(grid):
    queue = deque([(0, 0, 1)])
    n = len(grid)       # 세로 길이
    m = len(grid[0])    # 가로 길이
    visited = [[False for j in range(m)] for i in range(n)]

    while queue:
        r, c, count = queue.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = True

        if r == n - 1 and c == m - 1:
            return count

        new_r, new_c = move_to_up_location(r, c)
        if new_r >= 0 and grid[new_r][new_c] != 0:
            queue.append((new_r, new_c, count + 1))

        new_r, new_c = move_to_down_location(r, c)
        if new_r < n and grid[new_r][new_c] != 0:
            queue.append((new_r, new_c, count + 1))

        new_r, new_c = move_to_left_location(r, c)
        if new_c >= 0 and grid[new_r][new_c] != 0:
            queue.append((new_r, new_c, count + 1))

        new_r, new_c = move_to_right_location(r, c)
        if new_c < m and grid[new_r][new_c] != 0:
            queue.append((new_r, new_c, count + 1))


    return -1

def move_to_up_location(row, column):
    return row - 1, column

def move_to_down_location(row, column):
    return row + 1, column

def move_to_left_location(row, column):
    return row, column - 1

def move_to_right_location(row, column):
    return row, column + 1

print (find_shortest_way(maps))     # 정답 11