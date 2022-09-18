from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        for i in range(1, len(height)):

            left_max[i] = max(height[i], left_max[i - 1])

        right_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        # print(left_max)
        # print(right_max)

        ans = 0
        for i in range(1, len(height) - 1):

            curr = min(left_max[i], right_max[i]) - height[i]

            ans += curr

            # print(f'curr: {curr}')

        return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4,2,0,3,2,5]
    # 9
    print(Solution().trap(height))
