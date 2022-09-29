from typing import List
import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if len(arr) == k:
            return arr

        left = bisect.bisect_left(arr, x) - 1
        right = left + 1

        # print(f'left: {left}, right: {right}')
        # print(f'right - left - 1: {right - left - 1}')

        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue

            if right == len(arr) or (abs(arr[left] - x) <= abs(arr[right] - x)):
                left -= 1
            else:
                right += 1

        # print(f'left: {left}, right: {right}')

        return arr[left + 1:right]


class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        sorted_dist_arr = sorted(arr, key=lambda num: abs(x - num))

        ans = sorted(sorted_dist_arr[:k])

        return ans


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = -1
    arr = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
    k = 3
    x = 5
    print(Solution().findClosestElements(arr, k, x))
