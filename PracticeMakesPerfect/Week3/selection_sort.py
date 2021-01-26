input = [4, 6, 2, 9, 1 ]
#        4
def selection_sort(array):
    l = len(array)
    for i in range(l - 1):
        min_index = i
        for j in range(l - i):
            if array[i+j]<array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]



selection_sort(input)
print(input)