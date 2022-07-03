from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = 1
        down = 1
        for i in range(1, len(nums)):

            if nums[i - 1] < nums[i]:
                up = down + 1
            elif nums[i - 1] > nums[i]:
                down = up + 1

        return max(up, down)


class Solution2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [0] * len(nums)
        down = [0] * len(nums)

        # Base case
        up[0] = 1
        down[0] = 1

        for i in range(1, len(nums)):

            if nums[i - 1] < nums[i]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]

            elif nums[i - 1] > nums[i]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]

            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[-1], down[-1])


class Solution1:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [0] * len(nums)
        down = [0] * len(nums)

        # up[0] = 1
        # down[0] = 1

        for i in range(1, len(nums)):

            for j in range(i):

                if nums[j] < nums[i]:
                    # j is previous index
                    up[i] = max(up[i], down[j] + 1)

                elif nums[j] > nums[i]:
                    down[i] = max(down[i], up[j] + 1)

        # print(f'up: {up}')
        # print(f'down: {down}')

        # return max(up[-1], down[-1])
        return 1 + max(up[-1], down[-1])


if __name__ == '__main__':
    nums = [1, 7, 4, 9, 2, 5]
    # 6
    nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    # 7
    # nums = [0, 0]
    # 1
    print(Solution().wiggleMaxLength(nums))
