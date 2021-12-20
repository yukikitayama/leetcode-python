from typing import List
import collections


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_element = min(arr)
        max_element = max(arr)
        shift = -min_element
        # e.g. max: 5, min: 2, line length: 5 - 2 + 1 = 4
        # e.g. max: 5, min: -2, line length: 5 + 2 + 1 = 8
        line = [0] * (max_element - min_element + 1)

        ans = []

        for num in arr:
            # =1 because arr values are distinct
            # + shift to use index 0 and no negative index
            # e.g. min: 2, num: 2, shift: -2, index: 2 - 2 = 0
            # e.g. min: -5, num: -5, shift: -(-5) = 5, index: -5 + 5 = 0
            line[num + shift] = 1

        min_diff = max_element - min_element
        prev = 0

        # +shift because curr range from 1 to shifted value
        for curr in range(1, max_element + shift + 1):

            if line[curr] == 0:
                continue

            # curr - prev is the diff of integers
            if curr - prev == min_diff:
                # -shift because prev and curr are after shift, but answer needs before shift
                ans.append([prev - shift, curr - shift])

            elif curr - prev < min_diff:
                ans = []
                ans.append([prev - shift, curr - shift])
                min_diff = curr - prev

            prev = curr

        return ans


class Solution3:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []

        min_diff = float('inf')

        for i in range(len(arr) - 1):
            curr_diff = arr[i + 1] - arr[i]

            if curr_diff == min_diff:
                ans.append([arr[i], arr[i + 1]])
            elif curr_diff < min_diff:
                ans = []
                ans.append([arr[i], arr[i + 1]])
                min_diff = curr_diff

        return ans


class Solution2:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []

        min_diff = float('inf')

        for i in range(len(arr) - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                ans.append([arr[i], arr[i + 1]])

        return ans


class Solution1:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        diff_to_pairs = collections.defaultdict(list)
        min_diff = float('inf')

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                diff = arr[j] - arr[i]

                if diff < min_diff:
                    min_diff = diff

                diff_to_pairs[diff].append([arr[i], arr[j]])

        return diff_to_pairs[min_diff]


"""
- Time
  - O(NlogN) + O(N^2)
"""


if __name__ == '__main__':
    arr = [4,2,1,3]
    print(Solution().minimumAbsDifference(arr))
