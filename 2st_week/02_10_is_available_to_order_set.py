# set을 이용한 문제풀이
# if - in 구절은 hash를 이용해 O(1) 만큼의 시간밖에 들지 않기 때문에, 이진 탐색의 O(lonN) 보다 효율적으로 계산할 수 있다.

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)