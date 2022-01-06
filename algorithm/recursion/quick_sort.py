def quick_sort(nums):
    n = len(nums)
    q_sort(nums, 0, n - 1)


def q_sort(nums, lo, hi):
    if lo < hi:
        p = partition(nums, lo, hi)
        # Left sublist
        q_sort(nums, lo, p - 1)
        # Right sublist
        q_sort(nums, p + 1, hi)


def partition(nums, lo, hi):
    # Pick the last element as a pivot
    pivot = nums[hi]

    i = lo
    for j in range(lo, hi):
        if nums[j] < pivot:
            # Swap
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    # ?
    nums[i], nums[hi] = nums[hi], nums[i]
    # Return the index of pivot value in the sorted array
    return i