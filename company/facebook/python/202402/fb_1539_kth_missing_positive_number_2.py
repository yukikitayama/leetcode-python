from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # arr[i] - i - 1 is the number of missing integers before arr[i]
        # arr: [2, 3, 4, 7, 11], [1, 2, 3, 4, 5]
        # arr[3] - 3 - 1 = 7 - 4 = 3, and [1, 5, 6] are missing before arr[3]

        left = 0
        right = len(arr) - 1

        # When terminating, left = right + 1
        while left <= right:
            mid = (left + right) // 2

            # Missing numbers aren't enough for k
            # so go to right for more missing
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1

        # arr[right] - right - 1 is the number of missing before arr[right]
        # so what we want is arr[right] + k and subtract the before missing number
        # to get the after arr[right]
        return arr[right] + k - (arr[right] - right - 1)

    def findKthPositive2(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k

        # arr[0]: 2, -1 because it doesn't include arr[0]
        k -= arr[0] - 1

        for i in range(len(arr) - 1):

            curr_missing = arr[i + 1] - arr[i] - 1

            if k <= curr_missing:
                return arr[i] + k

            k -= curr_missing

        # If still k
        return arr[-1] + k

    def findKthPositive1(self, arr: List[int], k: int) -> int:

        expected = 1

        # Edge case
        while k > 0 and arr[0] != expected:
            k -= 1
            if k == 0:
                return expected
            expected += 1

        if k == 0:
            return expected

        for i in range(len(arr)):
            if arr[i] == expected:
                expected += 1
            else:
                while k > 0 and arr[i] != expected:
                    k -= 1
                    if k == 0:
                        return expected
                    expected += 1

                expected += 1

        # Edge case
        if k > 0:
            return arr[-1] + k
