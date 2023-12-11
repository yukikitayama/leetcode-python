from typing import List
import bisect


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = int(len(arr) * 0.25)

        curr_num = arr[0]
        curr_count = 1

        for i in range(1, len(arr)):

            if arr[i] != curr_num:
                curr_num = arr[i]
                curr_count = 1
            else:
                curr_count += 1

                if curr_count > threshold:
                    return arr[i]

        return arr[0]


class Solution2:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [
            arr[n // 4],
            arr[n // 2],
            arr[3 * n // 4]
        ]
        target = n / 4

        for candidate in candidates:
            left = bisect.bisect_left(arr, candidate)
            right = bisect.bisect_right(arr, candidate) - 1

            # print(f"left: {left}, right: {right}")

            if right - left + 1 > target:
                return candidate

        return -1


if __name__ == "__main__":
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    # arr = [1]
    print(Solution().findSpecialInteger(arr))
    print(Solution2().findSpecialInteger(arr))
