import bisect

nums = [1, 2, 3]
print(bisect.bisect_left(nums, 1))  # 0
print(bisect.bisect_left(nums, 4))  # 3
print(bisect.bisect_right(nums, 1))  # 1
print(bisect.bisect(nums, 1))  # 1
print(bisect.bisect(nums, 4))  # 3
letters = ['c', 'f', 'j']
print(bisect.bisect_right(letters, 'd'))  # 1
print(bisect.bisect_left(letters, 'd'))  # 1
print(bisect.bisect_right(letters, 'c'))  # 1
print(bisect.bisect_left(letters, 'c'))  # 0
print(bisect.bisect_right(letters, 'z'))  # 3
print(bisect.bisect_right(letters, 'z') % len(letters))  # 0
