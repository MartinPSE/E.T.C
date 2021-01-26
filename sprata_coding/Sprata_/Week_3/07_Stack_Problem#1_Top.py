top_heights = [6, 9, 5, 7, 4]

# 맨 뒤에꺼 없어져 ? Update 됨? -> Stack!
# <- <- <- <- <-
# 6  9  5  7  4
#[0  0  0  0  0]


#[0  0  2  2  4]

#  for idx in range(4, 0, -1):    # range(시작 , 끝나는 점 , 연산의 조건)
#     print(idx)

# O(N^2)  의 시간복잡도


def get_receiver_top_orders(heights):
        answer = [0] * len(heights)
        while heights:  # heights 가 빈 상태가 아닐때까지     O(N)
            height = heights.pop()
            # [6, 9, 5, 7]
            for idx in range(len(heights) - 1, 0, -1):  # index  니깐     O(N)

                if heights[idx] > height:  # Laser가 박히는 순간
                    answer[len(heights)] = idx + 1  # 결국 자리에 넣어주는거야!
                    break
        return answer


print(get_receiver_top_orders(top_heights))



