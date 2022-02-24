"""
- If arr[mid] is greater than mid, search to the left
- If arr[mid] is smaller than mid, search to the right
"""


from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == mid:
                answer = mid
                # Sill continue to search because we need to find the smallest index
                right = mid - 1

            elif arr[mid] < mid:
                left = mid + 1

            else:
                right = mid - 1

        return answer


if __name__ == '__main__':
    arr = [-10, -5, 0, 3, 7]
    # 3
    print(Solution().fixedPoint(arr))
