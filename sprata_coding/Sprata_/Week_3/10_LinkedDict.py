# index 값이 동일한 경우가 생길 수 밖에 없어.
# Dict  에서 발생하는 충돌을 Linkedlist  를 이용해서 해결
# key 는 꼭 필히 저장해줘야한다.
# 체이닝! Chaining!

class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:  # key / value 를 ---> Data  안에서 찾자!
            if key == k:  # 동일 한 key 가 발생하면
                return v  # value 값 return


class LinkedDict:
    def __init__(self):
        self.items = []  # LinkedTuple .... n개
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)
