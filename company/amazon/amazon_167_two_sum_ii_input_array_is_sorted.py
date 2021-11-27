from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        low = 0
        high = len(numbers) - 1

        while low < high:
            sum = numbers[low] + numbers[high]

            if sum == target:
                # +1 because the 1-indexed array of integers
                return [low + 1, high + 1]

            # Increase the next sum by increment lower index because numbers is increasing order
            elif sum < target:
                low += 1

            # If the current sum exceeded the target, decrement higher index to reduce the next sum
            else:
                high -= 1

        # In case there's no solution
        return [-1, -1]


numbers = [2,7,11,15]
target = 9
numbers = [2,3,4]
target = 6
print(Solution().twoSum(numbers, target))

