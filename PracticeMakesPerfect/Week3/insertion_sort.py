input = [4, 6, 2, 9, 1, 7]


#  4,6
#  4,6,2 -> 2,4,6
#  4,6,2,9 -> 2,4,6,9
#  4,6,2,9,1 -> 1,2,4,6,9

def insertion_sort(array):
    l = len(array)
    for i in range(1, l):
        end = i
        while end > 0 and array[end - 1] > array[end]:
            array[end - 1], array[end] = array[end], array[end - 1]
            end -= 1


insertion_sort(input)
print(input)
