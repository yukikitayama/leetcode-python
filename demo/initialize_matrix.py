r = 2
c = 3

mat1 = [[0] * c] * r
mat2 = [[0 for _ in range(c)] for _ in range(r)]

print('1')
for row in mat1:
    print(row)
print()

print('2')
for row in mat2:
    print(row)
print()

queue1 = [1, 2, 3, 4, 5, 6]
queue2 = [1, 2, 3, 4, 5, 6]

for i in range(r):
    for j in range(c):
        mat1[i][j] = queue1.pop(0)
print('1')
for row in mat1:
    print(row)
print()

for i in range(r):
    for j in range(c):
        mat2[i][j] = queue2.pop(0)
print('2')
for row in mat2:
    print(row)
print()

print(f'id(mat1[0]): {id(mat1[0])}, id(mat1[1]): {id(mat1[1])}')
print(f'id(mat2[0]): {id(mat2[0])}, id(mat2[1]): {id(mat2[1])}')