from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 1
        anchor = 0

        for i in range(1, N):
            # if i != N-1:
            #     print(f'arr[i - 1]: {arr[i - 1]}, arr[i]: {arr[i]}, arr[i + 1]: {arr[i + 1]}')

            c = self.compare(arr[i - 1], arr[i])
            # if i != N-1:
            #     c_next = self.compare(arr[i], arr[i + 1])
            #     print(f'c: {c}, c_next: {c_next}')

            if c == 0:
                anchor = i

            # arr: [1, 2, 1]
            # c: compare(arr[0], arr[1]) = compare(1, 2) = -1
            # compare(arr[1], arr[2]) = compare(2, 1) = 1
            # -1 * 1 = -1
            # Last two element or when alternating sequence ends
            # When alternating c * compare() = -1
            elif i == N - 1 or c * self.compare(arr[i], arr[i + 1]) != -1:
                # anchor is left pointer, and i is right pointer
                ans = max(ans, i - anchor + 1)
                # print(f'ans: {ans}, anchor: {anchor}, i: {i}')
                anchor = i

        return ans

    def compare(self, x: int, y: int) -> int:
        if x < y:
            c = -1
        elif x > y:
            c = 1
        else:
            c = 0
        return c


"""
Time complexity
Let n be the length of arr. O(n) because it scans from left to right

Space complexity
O(1)
"""


arr = [9,4,2,10,7,8,8,1,9]
print(Solution().maxTurbulenceSize(arr))
