genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


# 4 1 3 0
# 장르별로 가장 많이 재생된 노래 두개 --> 총 4개
# 속한 노래가 많이 재생된 장르 먼저 수록 --> 각각의 plays 의 총합 pop,
# 장르 내에서 많이 재생된 노래를 먼저 수록 -->  pop[4] / pop[1] / classic[3] / classic[0]
# 장르 내에서 재생 횟수가 같은 노래중에서는 index 가 낮은 노래를 먼저 수록

# zip 함수를 이용해서 dict로 합쳐버리기 zip(key, value)
#

def get_melon_best_album(genre_array, play_array):
    answer = []
    dicts = {}
    for g, p in zip(genre_array, play_array):
        if g in dicts.keys():
            dicts[g] += p
        else:
            dicts[g] = p

    dicts = sorted(dicts.items(), key=lambda x: x[1], reverse=True)

    while dicts:
        dic = {}
        dict = dicts.pop()
        for i in range(len(genre_array)):
            if dict[0] == genre_array[i]:
                dic[i] = play_array[i]
        dic = sorted(dic.items(), reverse=True, key=lambda x: x[1])
        print(dic)
        if len(dic) == 1:
            answer.append(dic[0][0])
        else:
            for j in range(2):
                answer.append(dic[j][0])
    return answer


print(get_melon_best_album(genres, plays))
