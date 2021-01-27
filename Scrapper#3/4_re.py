import re

p = re.compile("ca.e")


# . 하나의 문자
# ^ (^de) 문자열의 시작 > desk, destiny | fade ( X )
# $ (se$) : 문자열의 끝 > case, base


def print_match(m):
    if m:
        print("m.group() :", m.group())
        print("m.string():",m.string)
        print("m.start(): " ,m.start())
        print("m.end(): ",m.end())
        print("m.span(): " , m.span())
    else:
        print("매칭되지 않음 ")

#
# m = p.match("careless")  # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)
#
# m = p.search("careless  ")
# print_match(m)

lst = p.findall("good care cafe") #
print(lst)