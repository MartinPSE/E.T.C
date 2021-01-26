# 알고리즘 3 주차
# 정렬!!
# 버블 정렬!!

list = [4, 6, 2, 9, 1]

# O(N) + O(N) = O(N^2)


def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(j)

    return


bubble_sort(list)



