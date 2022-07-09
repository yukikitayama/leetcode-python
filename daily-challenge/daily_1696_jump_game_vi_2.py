"""
- DP
- Two pointers
"""


from typing import List
import collections


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = [0] * n
        score[0] = nums[0]
        dq = collections.deque()
        dq.append(0)
        for i in range(1, n):

            # print(f'i: {i}, dq: {dq}')

            # Pop out-of-range index, because we cannot use
            while dq and dq[0] < i - k:
                dq.popleft()
                # print(f'    out-of-range pop')

            score[i] = score[dq[0]] + nums[i]
            # print(f'  score after update: {score}')

            # Pop smaller value
            while dq and score[i] >= score[dq[-1]]:
                dq.pop()
                # print(f'    small value pop')

            dq.append(i)

            # print(f'  dq: {dq}')
            # print(f'  score: {score}')

        return score[-1]


if __name__ == '__main__':
    nums = [1, -1, -2, 4, -7, 3]
    k = 2
    # 7
    # nums = [10, -5, -2, 4, 0, 3]
    # k = 3
    # 17
    print(Solution().maxResult(nums, k))
