# <문제> 상하좌우
# 여행가 A 는 N * N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 x 1 크기의 정사각형
# 가장 왼쪽 위 좌표는 (1,1) 이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당합니다.
# 여행가 A 는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상(1,1)
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로
# L : 왼쪽 , R: 오른쪽 , U : 위로 한칸 , D: 아래로 한칸

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ["L", "R", "U" ,"D"]

for plan in plans: # L , R , U , D
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)
