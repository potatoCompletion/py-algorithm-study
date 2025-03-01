from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# 상 = 0, 하 = 1, 좌 = 2, 우 = 3
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# R과 B의 위치를 찾는다.
# 해당 위치를 딕셔너리 형태로 각각 저장한다.
# 빼내서 위치 비교하고 이동

def is_available_to_take_out_only_red_marble(game_map):
    count = 0
    n = len(game_map)
    m = len(game_map[0])
    red_r, red_c, blue_r, blue_c = 0, 0, 0, 0
    visited = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_r, red_c = i, j
            if game_map[i][j] == "B":
                blue_r, blue_c = i, j

    direction_list = [
        (-1, 0),    # 상
        (1, 0),     # 하
        (0, -1),    # 좌
        (0, 1)      # 우
    ]

    queue = deque([(red_r, red_c, blue_r, blue_c, 0)])

    while queue:
        red_r, red_c, blue_r, blue_c, count = queue.popleft()

        for i in range(4):


        for nr, nc in direction_list:
            if count > 9:
                continue


            new_red_r, new_red_c, new_blue_r, new_blue_c = red_r + nr, red_c + nc, blue_r + nr, blue_c + nc
            next_red_str = game_map[new_red_r][new_red_c]
            next_blue_str = game_map[new_blue_r][new_blue_c]

            if next_red_str == "O":
                return True

            if next_blue_str == "#":
                new_blue_r, new_blue_c = blue_r, blue_c

            if next_red_str == "B" and new_blue_r == blue_r:
                continue

            if next_red_str != "#" and next_blue_str != "O":
                game_map[red_r][red_c] = "#"
                if new_blue_r != blue_r:
                    game_map[blue_r][blue_c] = "."

                queue.append((new_red_r, new_red_c, new_blue_r, new_blue_c, count + 1))

    return False

def can_append(red_r, red_c, blue_r, blue_c, direction, queue):
    while True:
        next_red_r, next_red_c = red_r + dr[direction], red_c + dc[direction]
        next_blue_r, next_blue_c = blue_r + dr[direction], blue_c + dc[direction]

        if

print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))