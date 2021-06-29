# ord() returns an integer representing the Unicode character
print(f'ord("a"): {ord("a")}')

ch = 'l'
diff = ord(ch) - ord('a')
print(f'difference: {diff} by ord("l"): {ord(ch)} - ord("a"): {ord("a")}')

# Returns bit number, e.g. e is 4 because a:0, b:1, c:2, d:3, e:4
bit_number = lambda ch: ord(ch) - ord('a')

bitmask = 0

s1 = 'leetcode'
for ch in s1:
    # x|= 3 is same as x = x | 3. | is bitwise operator OR
    bitmask |= 1 << bit_number(ch)
    print(f'bitmask: {bitmask}, '
          f'bit_number(ch): {bit_number(ch)}, '
          f'{1 << bit_number(ch)}')


def no_common_letters(s1, s2):
    bit_number = lambda ch: ord(ch) - ord('a')
    bitmask1 = bitmask2 = 0
    for ch in s1:
        bitmask1 |= 1 << bit_number(ch)
    for ch in s2:
        bitmask2 |= 1 << bit_number(ch)
    print(f'bitmask1: {bitmask1}, bitmask2: {bitmask2}')
    return bitmask1 & bitmask2 == 0


print(no_common_letters('leetcode', 'leetcode'))
print(no_common_letters('leetcode', 'yuki'))
print(no_common_letters('leetcode', 'code'))
print(bin(542748))
