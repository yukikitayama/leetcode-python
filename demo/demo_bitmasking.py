characters = 'abc'
n = len(characters)
k = 2
for bitmask in range(1 << n):
    print(f'bitmask: {bitmask}, bin(bitmask): {bin(bitmask)}')

    if bin(bitmask).count('1') == k:
        for i in range(n):
            # e.g. n: 3, i: 0, n - 1 - i: 2, Third bit from the right '1'00
            # i: 1, n - 1 - i: 1, Second bit from the right 0'1'0
            # i: 2, n - 1 - i: 2, First bit from the right 00'1'
            if bitmask & (1 << n - 1 - i):
                print(f'  i: {i}, characters[i]: {characters[i]}')