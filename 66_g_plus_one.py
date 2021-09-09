from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i

            if digits[idx] == 9:
                digits[idx] = 0

            else:
                digits[idx] += 1
                return digits

        # If it's reached here, all the digits were nine
        return [1] + digits


"""
Time complexity
Let n be the length of digits. O(n) to for loop from right to left

Space complexity
In the final return statement, it creates a new list, so O(n + 1) = O(n)
"""


digits = [1,2,3]
digits = [9]
print(Solution().plusOne(digits))
