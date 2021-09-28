q = [0]

for i in range(5):

    print(f'i: {i}')

    if i == 2:
        print(f'continue')
        continue

    for j in range(5, 10):

        print(f'  j: {j}')