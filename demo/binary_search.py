import bisect


nums = [1, 2, 3, 4, 5]


index = bisect.bisect_left(nums, 3)
print(f'index: {index}')

index = bisect.bisect_right(nums, 3)
print(f'index: {index}')

index = bisect.bisect_left(nums, 3, 1, len(nums))
print(f'index: {index}')

index = bisect.bisect_left(nums, 6, 1, len(nums))
print(f'index: {index}')


def binary_search(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


