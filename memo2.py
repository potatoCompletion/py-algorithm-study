# 최소 턴 수 리턴
# k 만큼 작은 수는 오름차순을 무시하고 낼 수 있음
# 1장 이상씩 내려놓을 수 있다
# cards1과 cards2를 각각 오름차순 정렬
# 한 사람이 카드 내려놓을 때를 1턴으로 계산, 번갈아가면서 1번 씩 냈다면 2턴

# 첫번째 방법 (실패)
# 1. 오름차순으로 냈을 때의 턴 수를 구한다.
# 2. 바꿀수있는 요쇼들을 바꿨을 때의 턴 수를 구한다.
# 3. 구한 답 중 작은 값 리턴

# 두번째 방법
# 1. 각각의 최댓값, 최소값을 구한다
# 2. 한쪽의 최대값이 한쪽의 최소값보다 작으면 전부 낸다
# 2-1. 그렇지 않으면, 최소값을 하나씩 뺀다
# 과정을 반복하며 turn을 구한다.

# 세번째 시도
# 1. cards1과 cards2 를 각각 돌며 바꿀수 있는 요소가 있는지 찾는다.
# 2. 바꾼 요소가 상대 카드 뭉치에서 몇번째에 위치하는지 파악한다. 상대 카드뭉치에 들어가서 정렬했을 때 직전 요소를 구한다. (ex. cards1의 마지막 요소 5, cards2 = [4,6] 이면 4 리턴. 최소값이면 0 리턴)
# 3. 만약 상대 카드 뭉치에서 최대값이라면 바꾸기

from collections import deque
import heapq

def solution(cards1, cards2, k):
    # 첫번째 시도 코드
    # turn = 0
    # all_cards = []
    # heap = []
    # can_change_queue = deque()
    #
    # for card in cards1:
    #     all_cards.append(card)
    #
    # for card in cards2:
    #     all_cards.append(card)
    #
    # all_cards.sort()
    # prev_player = -1
    #
    # for i in range(len(all_cards)):
    #     if all_cards[i] + k in all_cards:
    #         can_change_queue.append((i, all_cards.index(all_cards[i] + k)))
    #
    #     if all_cards[i] in cards1:
    #         if prev_player != 1:
    #             turn += 1
    #             prev_player = 1
    #     else:
    #         if prev_player != 2:
    #             turn += 1
    #             prev_player = 2
    #
    # heapq.heappush(heap, turn)
    #
    # while can_change_queue:
    #     turn = 0
    #     first_change_index, second_change_index = can_change_queue.popleft()
    #     all_cards[first_change_index], all_cards[second_change_index] = all_cards[second_change_index], all_cards[first_change_index] # 바꾸기
    #
    #     for i in range(len(all_cards)):
    #         if all_cards[i] in cards1:
    #             if prev_player != 1:
    #                 turn += 1
    #                 prev_player = 1
    #         else:
    #             if prev_player != 2:
    #                 turn += 1
    #                 prev_player = 2
    #
    #     heapq.heappush(heap, turn)
    #     all_cards[first_change_index], all_cards[second_change_index] = all_cards[second_change_index], all_cards[first_change_index] # 원상복구
    #
    # return heapq.heappop(heap)


    turn = 0
    heap = []
    cards1.sort()
    cards2.sort()

    while len(cards1) == 0 or len(cards2) == 0:
        cards1_min = cards1[0]
        cards1_max = cards1[-1]
        cards2_min = cards2[0]
        cards2_max = cards2[-1]


        if cards1_min < cards2_min:
            temp_cards1 = cards1.copy()
            while len(temp_cards1) == 0:
                for i in range(1, len(temp_cards1)):
                    card1_target = temp_cards1[-i]

                    if card1_target < cards2_min:
                        temp_cards1 = temp_cards1[:i]
                        turn += 1


    return heapq.heappop(heap)

solution([1, 3, 5, 7], [2, 4, 6, 8], 6)
# 88 91
# 90 80