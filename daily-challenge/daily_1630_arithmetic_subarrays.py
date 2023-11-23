from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_arithmetic(arr):
            arr.sort()
            diff = arr[1] - arr[0]

            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False

            return True

        ans = []

        for i in range(len(l)):
            arr = nums[l[i]:r[i] + 1]
            ans.append(is_arithmetic(arr))

        return ans


class SolutionOptimized:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_arithmetic(arr):
            min_num = min(arr)
            max_num = max(arr)
            set_arr = set(arr)
            diff = (max_num - min_num) / (len(arr) - 1)

            if int(diff) != diff:
                return False

            curr = min_num + diff
            while curr < max_num:
                if curr not in set_arr:
                    return False
                curr += diff

            return True

        ans = []

        for i in range(len(l)):
            arr = nums[l[i]: r[i] + 1]
            ans.append(is_arithmetic(arr))

        return ans


if __name__ == "__main__":
    nums = [4, 6, 5, 9, 3, 7]
    l = [0, 0, 2]
    r = [2, 3, 5]
    print(Solution().checkArithmeticSubarrays(nums, l, r))
