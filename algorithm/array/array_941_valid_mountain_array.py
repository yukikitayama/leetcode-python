from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        i = 0

        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1

        # print(f'i: {i}')

        if i == 0 or i == len(arr) - 1:
            return False

        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1

        return i == len(arr) - 1


if __name__ == '__main__':
    arr = [0, 3, 2, 1]
    print(Solution().validMountainArray(arr))
