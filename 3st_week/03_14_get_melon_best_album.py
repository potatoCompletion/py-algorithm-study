from collections import deque
# 멜론 베스트 앨범 구하기

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다. (단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.

# 일단 장르의 총 합을 구해야 한다. 어차피 전부 더해야 하므로 반복문 사용
# 그리고 내림차순으로 정렬해서 반복문을 돌린다.
# 타겟 장르에 해당하는 인덱스를 내림차순으로 다시 정렬한다.
# 정답 어레이에 넣는다. (반복)

def get_melon_best_album(genre_array, play_array):
    # 1. 반복문 많이 사용한 첫번째 풀이 코드 (곡이 한곡만 있는 경우를 생각 못해 틀린 코드)
    # answer = []
    # play_sum_dict = {}
    #
    # genre_set = set(genre_array)
    # for genre in genre_set:
    #     play_sum_dict[genre] = 0
    #
    # for i in range(len(genre_array)):
    #     play_sum_dict[genre_array[i]] += play_array[i]
    #
    # while play_sum_dict:
    #     high_play_sum = -1
    #     high_play_genre = ""
    #     for key in play_sum_dict.keys():
    #         if play_sum_dict[key] > high_play_sum:
    #             high_play_sum = play_sum_dict[key]
    #             high_play_genre = key
    #
    #     added_num = 0
    #     first_play = -1
    #     first_play_index = -1
    #     second_play = -1
    #     second_play_index = -1
    #
    #     for i in range(len(genre_array)):
    #         if genre_array[i] == high_play_genre:
    #             if play_array[i] > first_play:
    #                 second_play = first_play
    #                 second_play_index = first_play_index
    #                 first_play = play_array[i]
    #                 first_play_index = i
    #             elif play_array[i] > second_play:
    #                 second_play = play_array[i]
    #                 second_play_index = i
    #
    #     answer.append(first_play_index)
    #     answer.append(second_play_index)
    #
    #     del play_sum_dict[high_play_genre]
    #
    # return answer


    # 2. 딕셔너리, sorted 위주로 사용한 두번째 풀이
    answer = []
    n = len(genre_array)
    genre_total_sum_dict = {}
    genre_index_and_play_dict = {}

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre in genre_total_sum_dict:
            genre_total_sum_dict[genre] += play
            genre_index_and_play_dict[genre].append((i, play))
        else:
            genre_total_sum_dict[genre] = play
            genre_index_and_play_dict[genre] = [(i, play)]

    for genre, play_sum in sorted(genre_total_sum_dict.items(), key=lambda item: item[1], reverse=True):
        sorted_genre_list = sorted(genre_index_and_play_dict[genre], key=lambda item: (item[1], -item[0]), reverse=True)
        print(sorted_genre_list)
        song_count = 0
        for index, play in sorted_genre_list:
            if song_count >= 2:
                break

            answer.append(index)
            song_count += 1

    return answer



print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))