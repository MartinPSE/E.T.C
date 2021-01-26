# 반복문으로

def binary(array, target, start, end):
    while start <= end:
        mid = ( start + end ) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n, target = map(int,input().split())
array = list(map(int,input().split()))

result = binary(array , target , 0, n-1)

if result == None:
    print("똑바로 써주세요")
else:
    print( result + 1 )

