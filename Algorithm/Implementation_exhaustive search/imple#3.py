# <문제> : 왕실의 나이트
# 행복 왕국의 왕실 정원은 체스판과 같은 8 X 8 좌표 평면. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
# 나이트는 말을 타고 있어서 L 자 형태로만 이동 가능 하고 정원 밖으로는 못나가

# 나이트는 특정 위치에서 2가지의 경우로 이동
# 수평으로 두칸 이동한뒤 수직으로 한칸이동
# 수직으로 두칸 이동한 뒤에 수평으로 한칸 이동


"""
idea1. ASCII 변환
idea2. 이동 따로 구현 해놓기 배열로 --> dx,dy로 해도 물론 가능
idea3. 체스판 나갈꺼 생각
"""

# 나이트 위치 입력 받고
input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0]) - ord('a')) + 1

result = 0

# 나이트 이동할 수 있는 8가지 방향 정의
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능?
for move in moves:
    # 위치 확인
    next_row = row + move[0]
    next_column = column + move[1]
    # 가능 하다면 카운트 += 1
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)