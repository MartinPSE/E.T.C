input = [4, 6, 2, 9, 1]

# def bubble_sort(array):
#     l = len(array)
#     for i in range(l-1):
#         for j in range(l-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#
#
#
#     return
#
# bubble_sort(input)
# print(input)

def bubble_sort(array):
    l = len(array)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return


bubble_sort(input)
print(input)