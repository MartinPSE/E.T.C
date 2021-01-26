genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def solution(genres, play):
    answer = []
    playsDict = {}
    d = {}
    for g, p in zip(genres, play):
        if g in playsDict.keys():
            playsDict[g] += p
        else:
            playsDict[g] = p

    genreSort = sorted(playsDict.items(), reverse=True, key=lambda x: x[1])

    for (genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in d[genre][:2]]

    return answer


print(solution(genres, plays))
