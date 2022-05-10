"""
- Use stack
"""


from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)

        stack = []

        for i, v in enumerate(heights):

            # print(f'i: {i}, v: {v}')

            # Last height is smaller than or equal to current height
            # Keep popping as long as previous person is smaller than last person
            # so left most person can see all the right person in increasing order of height
            while stack and heights[stack[-1]] <= v:
                idx = stack.pop()
                # Right person is higher so it can see it, so increment
                ans[idx] += 1

            # stack[-1] was not popped above, because stack[-1] is higher than current height v
            # so increment it
            if stack:
                # print(f'  stack[-1]: {stack[-1]}')
                ans[stack[-1]] += 1

            stack.append(i)

            # print(f'  stack: {stack}, ans: {ans}')

        return ans


if __name__ == '__main__':
    heights = [10, 6, 8, 5, 11, 9]
    # [3, 1, 2, 1, 1, 0]
    print(Solution().canSeePersonsCount(heights))
