# 삽입정렬
# 이미 정돈되어있는 Data  에 삽입해서 정렬 한다.


input = [4, 6, 2, 9, 1]


# 4, 6
# 4, 6 ,2
# 4, 6, 2, 9
# 4, 6, 2, 9 , 1
# 삽입정렬 -> 조금 정렬이 되어있는 시스템에서 사용해보자!


# 추가할 곳이 없네? 바로 끝내버리자!
# [1,2,3,4,5]
# O(N) 만큼의 최선의 시간복잡도.


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):  # 1 -> (1,5)
        print("i는", i, "<-이것이다")
        for j in range(i):  # in 1
            print("j는", j, "<-이것이다")
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]


            else:
                break
    print(array)


insertion_sort(input)
