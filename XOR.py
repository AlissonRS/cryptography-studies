def xor(x, s):
    print(x, 'xor', s, '=', x ^ s)


def bxor(x, s):
    print(bin(x), 'xor', bin(s), '=', bin(x ^ s))


xor(4, 8)
xor(4, 4)
xor(255, 1)
xor(255, 128)
print()
bxor(4, 8)
bxor(4, 4)
bxor(255, 1)
bxor(255, 128)
