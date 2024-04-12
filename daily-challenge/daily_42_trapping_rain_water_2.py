from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        ans = 0

        while left < right:

            # Check which end to be updated
            if height[left] < height[right]:

                # Heigher height, so no trapping water
                if height[left] >= left_max:
                    left_max = height[left]

                # Lower height, so trap water
                else:
                    ans += left_max - height[left]

                left += 1

            if height[left] >= height[right]:

                # Heigher height, so no trapping water
                if height[right] >= right_max:
                    right_max = height[right]

                # Lower height, so trap water
                else:
                    ans += right_max - height[right]

                right -= 1

        return ans

    def trap1(self, height: List[int]) -> int:
        left_max = []
        max_so_far = 0
        for i in range(len(height)):
            max_so_far = max(max_so_far, height[i])
            left_max.append(max_so_far)

        right_max = []
        max_so_far = 0
        for i in range(len(height) - 1, -1, -1):
            max_so_far = max(max_so_far, height[i])
            right_max.append(max_so_far)
        right_max.reverse()

        trap = []
        for i in range(len(left_max)):
            trap.append(min(left_max[i], right_max[i]))

        # print(height)
        # print(trap)

        ans = 0
        for i in range(len(height)):
            ans += trap[i] - height[i]

        return ans
