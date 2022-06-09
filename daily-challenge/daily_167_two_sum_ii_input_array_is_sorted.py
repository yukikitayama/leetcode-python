"""
- Two pointers?
"""


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            curr = numbers[i] + numbers[j]

            if curr == target:
                return [i + 1, j + 1]
            elif curr < target:
                i += 1
            else:
                j -= 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    # [1,2]
    numbers = [2, 3, 4]
    target = 6
    # [1,3]
    print(Solution().twoSum(numbers, target))
