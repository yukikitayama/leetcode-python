from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()

        counts = []
        current_run = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                current_run += 1
                continue
            # When same numbers stop, append the result
            counts.append(current_run)
            # Reset counting
            current_run = 1
        counts.append(current_run)
        # print(counts)

        counts.sort(reverse=True)

        numbers_removed_from_arr = 0
        set_size = 0

        for count in counts:
            numbers_removed_from_arr += count
            set_size += 1
            if numbers_removed_from_arr >= (len(arr) // 2):
                break

        return set_size


# arr = [3,3,3,3,5,5,5,2,2,7]
# arr = [7,7,7,7,7,7]
# arr = [1,9]
# arr = [1000,1000,3,7]
arr = [1,2,3,4,5,6,7,8,9,10]
print(Solution().minSetSize(arr))
