from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        # Walk up
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be edge
        if i == 0 or i == n - 1:
            return False

        # Walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1


if __name__ == '__main__':
    arr = [2, 1]
    arr = [3, 5, 5]
    arr = [0, 3, 2, 1]
    print(Solution().validMountainArray(arr))
