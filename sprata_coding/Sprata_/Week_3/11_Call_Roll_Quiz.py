all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]
# 반복문 2번 사용해도 물론 가능, 하지만 O(N^2) 만큼 시간복잡도.



#  { 다 넣어} -> { key , key , key, key , } -> 하나둘씩 제거 하면 - > {key} 이 남는놈이 안온애잖아!
# 해쉬는 공간을 많이 사용하는대신 시간을 극대화 할 수 있어!!



def get_absent_student(all_array, present_array):
    dicts = {}
    for key in all_array:  # O(N)
        dicts[key] = True  # 공간복잡도도 O(N)

    for key in present_array:  # O(N)
        del dicts[key]

    for key in dicts.keys():
        return key


print(get_absent_student(all_students, present_students))

