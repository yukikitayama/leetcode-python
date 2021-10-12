text = 'test'
x = text.ljust(5)
print(len(x))
print(f'x: {x}.')

cur = []
cur += ['test']
print(cur)
cur += ['is']
print(cur)

text = 'test'
print(text[:0] + text[1:])
print()
for i in range(len(text)):
    print(text[:i] + text[i + 1:])