# Main function
def merge_sort(nums):

    # Bottom case
    # Empty list or length one list
    if len(nums) <= 1:
        return nums

    # Divide
    pivot = int(len(nums) / 2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])

    # Conquer and combine in a sorted order
    return merge(left_list, right_list)


# Helper function to merge in ascending order
def merge(left_list, right_list):
    # Index to iterate each list
    left_cursor = right_cursor = 0
    # Sorted list to return
    ret = []

    while left_cursor < len(left_list) and right_cursor < len(right_list):

        # If left item is smaller, append left item for ascending order
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1

        # If right item is smaller or equal, append right item for ascending order
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1

    # At here, either left_cursor or right_cursor reached the end
    # so either gives us None
    ret.extend(left_list[left_cursor])
    ret.extend(right_list[right_cursor])

    return ret
