import functools
import itertools


nums = [1, 2, 3, 4, 5]

result = functools.reduce(lambda x, y: x * y, nums)
# 1 * 2 * 3 * 4 * 5 = 6 * 20 = 120
print(f'result: {result}')

data = ['a', 'b', 'c']
result = functools.reduce(lambda x, y: x + y, data)
print(f'result: {result}')


def my_add(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')
    return result


def main():

    numbers = [0, 1, 2, 3, 4]

    functools.reduce(my_add, numbers)

    functools.reduce(my_add, numbers, 100)

    try:
        functools.reduce(my_add, [])
    except:
        print('Empty iterable fails without initializer')
        # The below return 0
        print(functools.reduce(my_add, [], 0))

    # Find max by reduce()
    nums = [3, 5, 2, 4, 7, 1]
    print(functools.reduce(lambda a, b: a if a > b else b, nums))

    # Boolean with reduce()
    print(functools.reduce(lambda a, b: bool(a and b), [1, 1, 1]))
    # Same as all([1, 1, 1])

    print(functools.reduce(lambda a, b: bool(a and b), [0, 1, 1]))
    # Same as all([0, 1, 1])

    # Reduce() any
    print(functools.reduce(lambda a, b: bool(a or b), [1, 0, 0]))
    print(any([1, 0, 0]))

    print(functools.reduce(lambda a, b: bool(a or b), [0, 0, 0]))
    print(any([0, 0, 0]))

    # Compared with accumulate()
    print(list(itertools.accumulate([1, 2, 3, 4], lambda a, b: a + b)))
    # [1, 3, 6, 10]
    print(functools.reduce(lambda a, b: a + b, [1, 2, 3, 4]))
    # 10


if __name__ == '__main__':
    main()
