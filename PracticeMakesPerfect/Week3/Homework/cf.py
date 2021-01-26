genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]





def solution(genres, plays):
    answer = []
    songs = {}

    for i in range(len(genres)):  # 1단계. 해시테이블songs key:genre, value:총합
        if genres[i] not in songs:
            songs[genres[i]] = plays[i]
        else:
            songs[genres[i]] += plays[i]
    songs = sorted(songs.items(), key=lambda item: item[1],reverse=True)  # value:총합 기준으로 sort
    print(songs)
    while songs:  # 2단계. 각 장르별로(위의 정렬된 해시테이블dic에서 pop()함) key: 고유번호, value:plays수
        dic = {}
        song = songs.pop()
        for i in range(len(genres)):
            if song[0] == genres[i]:
                dic[i] = plays[i]
        dic = sorted(dic.items(), reverse=True, key=lambda item: item[1])  # value 내림차순으로 정렬한거
        print(dic)
        if len(dic) == 1:  # 주의할점 : 1개일 땐 그냥 1개 출력
            answer.append(dic[0][0])
        else:
            for j in range(2):  # 많은 2개 출력
                answer.append(dic[j][0])

    return answer

result = solution(genres,plays)
print(result)