# <문제> 개미 전사
# 개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 한다.
# 메뚜기 마을에는 여러 개의 식량창고가 있는데 식량창고는 일직선으로 이어져 있다.
# 각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정
# 이때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.
# 따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량 창고를 약탈해야한다.

# EX) 창고0 창고1 창고2 창고3
#      1     3    1     5
# 개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성

import time
start_time = time.time()

N = int(input())
food_list = list(map(int,input().split()))
"""
My answer
# result1 = 0
# result2 = 0
# for i in range(len(food_list)):
#     if i % 2 == 0:
#         result1 += food_list[i]
#     else:
#         result2 += food_list[i]
# end_time = time.time()
# print (max(result1,result2))
# print(end_time-start_time)
"""

d = [0] * 100
d[0] = food_list[0]
d[1] = max(food_list[0],food_list[1])
for i in range(2,N):
    d[i] = max(d[i-1],d[i-2] + food_list[i])

end_time = time.time()
print(end_time - start_time)
print(d[N-1])