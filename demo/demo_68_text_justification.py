maxWidth = 16

# cur = ['This', 'is', 'an']
cur = ['This']

num_of_words = 0
for word in cur:
    num_of_words += len(word)

print(f'len(cur): {len(cur)}, num_of_words: {num_of_words}')

print(f'  0 % 1: {0 % 1}')
print(f'  1 % 1: {1 % 1}')
print(f'  2 % 1: {2 % 1}')
#
# print(f'  0 % 0: {0 % 0}')
# print(f'  1 % 0: {1 % 0}')

print(f'    0 or 1: {0 or 1}')
print(f'    2 or 1: {2 or 1}')

# for i in range(maxWidth - num_of_words):
#     print(f'  i % (len(cur) - 1): {i % (len(cur) - 1)}')