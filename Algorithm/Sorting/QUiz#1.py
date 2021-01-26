# <문제> 두 배열의 원소 교체
# 형석이는 2개의 배열 A와 B를 가지고 있습니다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수
# 형석이는 '최대 N번의 바꿔치기' 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는
# 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
# 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며,
# N,K 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K 번 바꿔치기 연산을 수행하여 만들 수 있는
# 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램

N, K = map(int, input().split())  # N, K 입력 받고
A = list(map(int, input().split()))  # A
B = list(map(int, input().split()))  # B


def change(A, B):
    A.sort()  # A 는 오름 차순
    B.sort(reverse=True)  # B 는 내림 차순
    # 첫 번째 인덱스부터 확인, 두 배열의 원소를 최대 K 번 비교
    for i in range(K):
        # A의 원소가 B의 원소보다 작은 경우
        if A[i] < B[i]:
            # 두 원소를 교체
            A[i], B[i] = B[i], A[i]
        else:  # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출
            break
    return print(sum(A))


change(A, B)
