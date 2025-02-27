k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]

# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 0 = 흰색, 1 = 빨간색, 2 = 파란색

# 각 색깔 별 동작 함수를 만든다.

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    count = 0
    max_column = len(game_map[0]) - 1
    max_row = len(game_map) - 1
    map_horse_status = {}

    for i in range(0, len(game_map)):
        for j in range(0, len(game_map[0])):
            map_horse_status[(i, j)] = []

    for i in range(0, horse_count):
        r, c, d = horse_location_and_directions[i]
        map_horse_status[(r, c)].append(i)

    while count <= 1000:
        count += 1

        for i in range(0, horse_count):
            horse = start_horse_location_and_directions[i]
            now_row, now_column = horse[0], horse[1]
            next_row, next_column = get_horse_next_location(horse)
            horse_num = i

            if (next_row < 0 or next_row > max_row) or (next_column < 0 or next_column > max_column) or game_map[next_row][next_column] == 2:
                next_row, next_column = get_opposite_location(horse)
                horse[2] = get_opposite_direction(horse[2])
                if (next_row < 0 or next_row > max_row) or (next_column < 0 or next_column > max_column) or game_map[next_row][next_column] == 2:
                    continue

            if game_map[next_row][next_column] == 0:
                change_horse_locations(map_horse_status[(now_row, now_column)], horse_num, start_horse_location_and_directions, next_row, next_column)
                move_to_white_space(map_horse_status[(now_row, now_column)], map_horse_status[(next_row, next_column)], horse_num)
            elif game_map[next_row][next_column] == 1:
                change_horse_locations(map_horse_status[(now_row, now_column)], horse_num, start_horse_location_and_directions, next_row, next_column)
                move_to_red_space(map_horse_status[(now_row, now_column)], map_horse_status[(next_row, next_column)], horse_num)

            if is_all_horse_in_same_place(horse_location_and_directions):
                return count


    return -1

def get_horse_next_location(horse):
    next_row = horse[0] + dr[horse[2]]
    next_column = horse[1] + dc[horse[2]]

    return next_row, next_column

def get_opposite_location(horse):
    next_row = horse[0] + (dr[horse[2]] * -1)
    next_column = horse[1] + (dc[horse[2]] * -1)

    return next_row, next_column

def get_opposite_direction(direction):
    if direction == 0:
        return 1
    if direction == 1:
        return 0
    if direction == 2:
        return 3
    if direction == 3:
        return 2

def is_all_horse_in_same_place(horse_location_and_directions):
    standard_horse_row = horse_location_and_directions[0][0]
    standard_horse_column = horse_location_and_directions[0][1]

    for i in range(1, len(horse_location_and_directions)):
        if standard_horse_row != horse_location_and_directions[i][0]:
            return False
        if standard_horse_column != horse_location_and_directions[i][1]:
            return False

    return True

def move_to_white_space(now_list, next_list, horse_num):
    index = now_list.index(horse_num)
    next_list.extend(now_list[index:])
    del now_list[index:]

def change_horse_locations(now_list, horse_num, start_horse_location_and_directions, next_row, next_column):
    index = now_list.index(horse_num)

    for horse_index in now_list[index:]:
        start_horse_location_and_directions[horse_index][0] = next_row
        start_horse_location_and_directions[horse_index][1] = next_column


def move_to_red_space(now_list, next_list, horse_num):
    index = now_list.index(horse_num)
    reverse_list = now_list[index:].reverse()
    next_list.extend(reverse_list)
    del now_list[index:]


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))