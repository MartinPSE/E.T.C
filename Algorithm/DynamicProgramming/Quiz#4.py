# <문제> 금광
# N * M 크기의 금광이 있다. 금광은 1 X 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있다.
# 채굴지는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
# 이후에 M -1 번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력 하는 프로그램을 출력


"""
idea1. 3가지의 경우
idea2. 세가지 경우 중에서 가장 많은 금을 가지고 있는 경우 -->
idea3. array[i][j] = i행 j열에 존재하는 금의 양
idea4. dp[i][j] = i행 j열까지의 최적의 해 ( 얻을 수 있는 금의 최댓 값)

dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j+1])

idea5. 범위 조건 주의.
idea6. 초기 데이터를 담는 변수 array 필요 X

"""

# TestCase 가 주어진다
for tc in range(int(input())):
    # N, M 을 입력받고
    n,m = map(int,input().split())
    # array 를 입력 받자
    array = list(map(int,input().split()))
    # 그 후 저장할 dp, 금고를 저장할 dp 하나 만들자
    dp = []
    index = 0  # array에서 금고 값 슬라이싱 용도 --> 리스트가 한줄로 주어졌으니 주의바람
    for i in range(n):
        dp.append(array[index:index+m])  # 0123,4567,891011
        index += m

    # 다이나믹 프로그래밍 들어가자.
    for j in range(1,m):
        for i in range(n):
            if i == 0 :
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n - 1:
                left_down =0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)
    result = 0

    for i in range(n):
        result = max (result , dp[i][m-1])
    print(result)
