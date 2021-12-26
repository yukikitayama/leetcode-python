from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1

        # Here left = right + 1, right < left
        # kth missing is between arr[right] and arr[left]
        # arr[right] - right - 1: the number of integers missing before arr[right]
        # so arr[right] + k - (arr[right] - right - 1)
        #  = k + right + 1
        # Because left = right + 1,
        return k + left


class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        # e.g. k: 2, arr[0]: 3
        if k < arr[0]:
            return k

        # e.g. k: 2, arr[0]: 2, k should be decremented by 1
        k -= arr[0] - 1

        for i in range(len(arr) - 1):

            # -1 because the minimum difference is one, but that's not missing
            # so make it 0
            curr_missing = arr[i + 1] - arr[i] - 1

            # e.g. k: 1, arr[i]: 2, arr[i]: 4, curr_missing: 1
            #      arr[i] + k: 3
            # e.g. k: 2, arr[i]: 2, arr[i]: 6, curr_missing: 3
            #      arr[i]+ k: 4
            if k <= curr_missing:
                return arr[i] + k

            # Filling into missing
            k -= curr_missing

        # If missing number is greater than arr[-1]
        return arr[-1] + k



