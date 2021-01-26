import collections

# collections.Counter()
# 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체이다.
# key (요소) : value (갯수)
# collections.Counter() 의 결과값(return)은 딕셔너리 형태로 출력된다.

# 1) 리스트(List)

lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']

print(collections.Counter(lst))

'''
결과 : 
Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})
'''
# ---------------------------------------------------------------------------------------------------------------------
# 또한 요소의 갯수가 많은 순으로 출력해준다.
print(collections.Counter({'가': 580, '나': 590, '다': 1200}))
'''
결과
Counter({'다': 1200, '나': 590, '가': 580})
'''
# ---------------------------------------------------------------------------------------------------------------------
# 값 = 개수 -> 형태로 입력이 가능하다.
print(collections.Counter(a=2, b=3, c=2))
'''
Counter({'b': 3, 'a': 2, 'c': 2})
        ['a','a','b','b','b','c','c]
'''
# ---------------------------------------------------------------------------------------------------------------------
# 문자열 {문자 : 개수} 의 딕셔너리 형태로 반환해준다.
container = collections.Counter()
container.update("sexyguysexyguy")
print(container)
'''
결과:
Counter({'y': 4, 's': 2, 'e': 2, 'x': 2, 'g': 2, 'u': 2})
'''
for k, v in container.items():
    print("key : {0} ---- value: {1}".format(k, v))
'''
key : s ---- value: 2
key : e ---- value: 2
key : x ---- value: 2
key : y ---- value: 4
key : g ---- value: 2
key : u ---- value: 2
'''
# ---------------------------------------------------------------------------------------------------------------------
# Counter 의 Method 들
# ---------------------------------------------------------------------------------------------------------------------
# 1. update() ---> Counter의 값을 갱신하자.
# 딕셔너리는 key, value 다 줘야하지만, Counter 는 문자열로만 넣어도 된다.

a = collections.Counter()
a.update("abbadfbdaf")
print(a)
'''
결과
Counter({'a': 3, 'b': 3, 'd': 2, 'f': 2})
'''
a.update({'f': 3, 'e': 2})  # 딕셔너리 는 이와 같은 형태로 update 해줘야함.
print(a)
# ---------------------------------------------------------------------------------------------------------------------
# 2. elements() --> 요소에 해당하는 값을 풀어서 반환
# 요소는 무작위로 반환, 1보다 작은 경우 출력하지 않는다.
# 대소문자 구분하며 , sorted() 이용하여 정렬가능.
b = collections.Counter()
b.update("Hello Python")
print(list(b.elements()))
# ['H', 'e', 'l', 'l', 'o', 'o', ' ', 'P', 'y', 't', 'h', 'n']
print(sorted(b.elements()))
# [' ', 'H', 'P', 'e', 'h', 'l', 'l', 'n', 'o', 'o', 't', 'y']
b2 = collections.Counter(a=4, b=2, c=0, d=-2)  # 마이너스는 못하네
print(list(b2.elements()))
# ['a', 'a', 'a', 'a', 'b', 'b']
# ---------------------------------------------------------------------------------------------------------------------
# 3. most_common() --> 요소들 중 빈도수가 높은 순으로 상위 N개를
# 리스트(list) 안에 튜플(tuple) 형태로 반환한다.
# ()을 입력하지 않는 경우, 요소 전체를 [('값', 개수)] 의 형태로 반환

c2 = collections.Counter('apple, orange, grape')
print(c2.most_common())
# [('a', 3), ('p', 3), ('e', 3), (',', 2), (' ', 2), ('r', 2), ('g', 2), ('l', 1), ('o', 1), ('n', 1)]
print(c2.most_common(3))  # ( 개수 ) 해당 하는 tuple 추출
# [('a', 3), ('p', 3), ('e', 3)]
# ---------------------------------------------------------------------------------------------------------------------
# 4. subtract()  ---> 말 그대로 뺀다!! 값이 - 이 나올 경우 마이너스 도출 x.subtract(y)  --> x - y
c2 = collections.Counter("Oh hyeong seok")
c3 = collections.Counter("Oh Yu K y e  o n g")
c3.subtract(c2)
print(c3)
# Counter({'h': 1, 'e': 1, 'o': 1, 's': 1, 'k': 1, 'O': 0, 'y': 0, 'n': 0, 'g': 0, 'Y': -1, 'u': -1, 'K': -1, ' ': -6})
# ---------------------------------------------------------------------------------------------------------------------
# 5. 덧셈 / 뺄셈 / 교집합(&) , 차집합(|) 가능!
# 단 뺄셈에서는 마이너스 도출 안한다.