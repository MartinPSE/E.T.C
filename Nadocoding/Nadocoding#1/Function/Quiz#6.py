# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#       * 함수명 : std_weight
#       * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# 출력예제
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        std = (height * 0.01) ** 2 * 22
        std_result = round(std, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, '%.2f' % std_result))
    elif gender == "여자":
        std2 = (height * 0.01) ** 2 * 21
        std2_result = round(std2, 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, '%.2f' % std2_result))


std_weight(178, "남자")
