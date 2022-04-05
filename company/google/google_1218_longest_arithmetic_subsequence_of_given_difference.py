from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        count = {}
        for a in arr:
            # print(f'a: {a}')
            # 1 because single element can be counted as a subsequence
            # get(a - difference) because we wanna find previously seen count
            # 0 because when we see it first time, we don't wanna count
            # This works because it's subsequence.
            # It doesn't work for subarray
            count[a] = 1 + count.get(a - difference, 0)
            # print(f'  count: {count}')

        return max(count.values())


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    difference = 1
    print(Solution().longestSubsequence(arr, difference))
