from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], right_max = right_max, max(arr[i], right_max)
        return arr


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    print(Solution().replaceElements(arr))
