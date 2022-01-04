from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        l = r = 0
        ret = []

        while l < len(left) and r < len(right):

            if left[l] < right[r]:
                ret.append(left[l])
                l += 1
            else:
                ret.append(right[r])
                r += 1

        ret.extend(left[l:])
        ret.extend(right[r:])

        return ret


if __name__ == '__main__':
    nums = [5, 2, 3, 1]
    print(Solution().sortArray(nums))
