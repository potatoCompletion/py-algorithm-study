# 이진탐색으로 풀이
# 결과는 나오지만 다음 파일에 이보다 더 효율적으로 set을 활용한 풀이가 있다.

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "치킨"]


def is_available_to_order(menus, orders):
    menus.sort()
    for menu in orders:
        first_target = 0
        end_target = len(menus)

        while True:
            target_index = (first_target + end_target) // 2
            if menus[target_index] == menu:
                break
            elif menus[target_index] < menu:
                first_target = target_index + 1
            elif menus[target_index] > menu:
                end_target = target_index - 1

            if first_target > end_target:
                return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)