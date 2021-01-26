import collections


input = "abace"

print(input.index("a"))

def find_not_repeating_character(string):
    d = collections.Counter(string)
    l = len(string)
    check = False
    for char in string:
        if d[char] == 1 and (string.index(char) <= l):
            check = True

            k = string.index(char)

    if check:
        return print(string[k])
    else:
        return '_'


result = find_not_repeating_character(input)
print(result)