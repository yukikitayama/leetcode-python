from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2

            # ?
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]

    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] > x:
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            elif arr[mid] == x:
                # Could have duplicate
                right = mid - 1

        # Here, left is left insertion point

        l = left - 1
        r = left
        # right: 2, left: 0, k: 1, right - left - 1: 1, already k found, so stop
        # right: 1, left: 0, k: 1, right - left - 1: 0, haven't reached k, so continue
        while r - l - 1 < k:

            if l == -1:
                r += 1
                continue

            if r != len(arr) and abs(x - arr[r]) < abs(x - arr[l]):
                r += 1
            else:
                l -= 1

        # l and r are exclusive
        return arr[l + 1:r]

    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key=lambda y: abs(x - y))

        ans = []
        for i in range(k):
            ans.append(sorted_arr[i])

        return sorted(ans)
