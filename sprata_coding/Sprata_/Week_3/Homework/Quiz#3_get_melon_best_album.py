# 멜론 베스트 앨범 뽑기
# 노래는 인덱스로 구분 / 장르별로 2개 씩
# Dict -> items ( Dict한방에 보여주기) -> sorted 함수 이용
# sorted(a.items(), key=lambda item:item[1])
# lambda 는 매개변수라고 생각하자. // 특정 인자를 받아서 어떤값으로 돌려줄지를 간단한 수식으로 표현


genres = ["classic", "pop", "classic", "classic", "pop"]  # 장르의 갯수 많은거 먼저
plays = [500, 600, 150, 800, 2500]  # 장르 내에서 많이 재생된 수 먼저 ! / 재생횟수 동일하면 index 값 순으로


# 장르 별로 곡의 정보 (인덱스, 재생횟수) 배열로 묶어 정리한다.
def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    print(genre_total_play_dict)
    print(genre_index_play_array_dict)
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_genre_play_array)
    result = []
    for genre, _value in sorted_genre_play_array:
        # [ 1,600 ] [ 4, 2500 ]
        index_play_array = genre_index_play_array_dict[genre]
        sorted_index_play_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        print(sorted_index_play_array)

        for i in range(len(sorted_index_play_array)):
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])

    return print(result)


get_melon_best_album(genres, plays)
