from typing import List
import collections


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        counter = collections.Counter(nums)

        ans = float('inf')
        max_so_far = 0

        for num in sorted(counter.keys()):

            # print(f'num: {num}, count: {counter[num]}')

            if num % 2 == 0:

                if counter[num] > max_so_far:
                    ans = num
                    max_so_far = max(max_so_far, counter[num])

            # print(f'  max_so_far: {max_so_far}')

        return -1 if ans == float('inf') else ans


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 4, 4, 1]
    nums = [4, 4, 4, 9, 2, 4]
    nums = [29, 47, 21, 41, 13, 37, 25, 7]
    print(Solution().mostFrequentEven(nums))
