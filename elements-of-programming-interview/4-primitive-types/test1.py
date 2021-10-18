def count_bits(x):
    num_bits = 0
    print(f'x: {x}, bin(x): {bin(x)}')
    while x:
        # Masking
        num_bits += x & 1
        print(f'  x & 1: {x & 1}')
        # Shifting
        x >>= 1
        print(f'  x: {x}, bin(x): {bin(x)}')
    return num_bits


print(count_bits(0))
print()

print(count_bits(1))  # 1 * 2^0
print()
"""
1 
"""

print(count_bits(2))  # 1 * 2^1 + 0 * 2^0
print()
print(count_bits(3))  # 1 * 2^1 + 1 + 2^0
print()
print(count_bits(4))  # Shoud be 1, because 1 * 2^2 + 0 * 2^1 + 0 * 2^0
print()
