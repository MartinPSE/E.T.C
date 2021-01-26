# < 구현 >
# 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정!!
# --> 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기는 어려운 문제
# Practice !!
for i in range(5):
    for j in range(5):
        print('(', i, ',', j, ')', end='')
    print()
# ---> 열
#  |  0,0 0,1 0,2 0,3 0,4
#  |  1,0
#  |  2,0
#  행

#  동 , 북 , 서 , 남
#  방향벡터 -> 로직설계
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 2,2

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[y]
    print(nx,ny)
