"""
https://stackoverflow.com/questions/14749415/how-to-use-single-colon-when-using-variable-for-slicing
https://stackoverflow.com/questions/1252357/is-there-an-object-unique-identifier-in-python
https://www.afternerd.com/blog/python-copy-list/

- Copying a python list means creating a new python object
- Slicing creates a new object
"""
nums = [1, 2, 3, 4, 5]
print(nums[1:4:1])
print(nums[1:4:None])
print(nums[1:4:])
print(nums[1:4])

nums1 = nums
print(nums1 is nums)
print(id(nums), id(nums1))
nums2 = nums[:]
print(nums2 is nums)
print(id(nums2), id(nums1))

print()

seq = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(f'seq: {seq}')
# Slice with all parameters specified
# start:1, stop:4, step:1
print(seq[1:4:1])

# Slice with default step value (default=1)
# start:1, stop:4, step:1
# All the following are equivalent
print(seq[1:4:None])
print(seq[1:4:])
print(seq[1:4])

# Slice with default stop value (default = len(seq))
# start:1, stop:len(seq), step:1
# All the following are equivalent
print(seq[1:None:1])
print(seq[1::1])

# Slice with default step and stop value
# start:1, stop:len(seq), step:1
# All the following are equivalent
print(seq[1:None:None])
print(seq[1::])
print(seq[1:])

# Slice with default start value
# start:1, stop:4, step:1
# All the following are equivalent
print(seq[None:4:1])
print(seq[:4:1])

# Slice with all default values
# start:1, stop:len(seq), step:1
# All the following are equivalent
print(seq[None:None:None])
print(seq[::])
print(seq[:])

