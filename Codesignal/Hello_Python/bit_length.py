n = 5
n.bit_length()  # 이렇게 활용할 수도 있고

# bit 수에 맞게 print를 하고 싶으면?
# 예를 들면 integer "5"을 0'b0101 네자리 표현을 하고 싶을 경우

BitLen = n.bit_length()  # bit length를 구하고 bit length는 3
BitLen = 4
Form = '0' + '{0}'.format(BitLen) + 'b'  # '04b'

print("Binary Format : 0'b{0}".format(format(n, Form)))