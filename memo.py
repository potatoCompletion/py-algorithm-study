import heapq

heights = [
        [3, 3, 3, 3, 3],
        [5, 5, 5, 5, 5]
    ]

result = []

def get_min_water_height(grid):

    find_way(0, grid, 0, 0)

    return heapq.heappop(result)

def find_way(water_height, grid, row, column):
    if row == len(grid) - 1 and column == len(grid[0]) - 1:
        return

    water_height += 1

    # 상,하,좌,우 갈 수 있는 곳 모두 시도
    if row - 1 >= 0 and grid[row - 1][column] < water_height:
        find_way(water_height, grid, row - 1, column)
    if row + 1 < len(grid) and grid[row + 1][column] < water_height:
        find_way(water_height, grid, row + 1, column)
    if column - 1 >= 0 and grid[row][column - 1] < water_height:
        find_way(water_height, grid, row, column - 1)
    if column + 1 < len(grid[0]) and grid[row][column + 1] < water_height:
        find_way(water_height, grid, row, column + 1)

    # 만약 여기까지 도달했다면 더 이상 갈 곳이 없다는 뜻. 이 때의 water_height를 저장
    heapq.heappush(result, water_height)

print(get_min_water_height(heights))