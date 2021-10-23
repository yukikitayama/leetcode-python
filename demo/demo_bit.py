# Left shift operator
print(1 << 0)  # 0
print(1 << 1)  # 10 = 1 * 2^1 = 2
print(1 << 2)  # 100 = 1 * 2^2 = 4
print(2 << 2)  # 2 * 2^2 = 8
print(3 << 4)  # 3 * 2^4 = 3 * 16 = 48

# Mask
print('Mask')
# mask = [1, 0, 1]
# index = 0
# print(mask[index] & 1)
# index = 1
# print(mask[index] & 1)
# index = 2
# print(mask[index] & 1)
mask = 0
# index = 0
# print(mask & (1 << index))
# index = 1
# print(mask & (1 << index))
# index = 2
# print(mask & (1 << index))
index = 0
print(mask | (1 << index))
index = 1
print(mask | (1 << index))
index = 2
print(mask | (1 << index))
print()
print(4 & (1 << 2))
