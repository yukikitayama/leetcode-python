import bisect


def BinarySearch(nums, target):
    i = bisect.bisect_left(nums, target)
    if i != len(nums) and nums[i] == target:
        return i
    else:
        return - 1

nums = [-1, 0, 1]
target = 1
# print(BinarySearch(nums, target))
# right most index
# print(bisect.bisect(nums, target))

nums = [[-1], [0], [1]]
target = [0]
# print(bisect.bisect(nums, target))

nums = [[-1, 0], [0, 5], [1, 6]]
# target = [0]  # 1
# target = [1]  # 2
# target = [1, 6]  # 3
# target = [0, 5]  # 2
target = [-1]  # 0
print(bisect.bisect(nums, target))