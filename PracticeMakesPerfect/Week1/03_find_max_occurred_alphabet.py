from collections import Counter

input = "hello my name is sparta 똥꼬 빨아라"



def find_max_occurred_alphabet(string):
        new_string = string.replace(" ", "")  # 공백을 없애는 아주 좋은 방법
        c = Counter(new_string)
        d = c.most_common(1)
        print(d)


find_max_occurred_alphabet(input)

# -------------------------------------------------------
# 교재방법
# str.isalpha() --> 이용해서 스트링인지? 아닌지?
