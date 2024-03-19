"""
When left > right, left denotes the index of the smallest character that is lexicographically greater than target. This is because all characters at indices greater than right would be greater than target and character immediately next to index right would be left (or right + 1) after the completion of binary search algorithm.
"""

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        while left <= right:

            mid = (left + right) // 2

            if letters[mid] == target:
                left = mid + 1
            elif letters[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

            # print(" ", left, right)

        # print(left)

        if left == len(letters):
            return letters[0]
        else:
            return letters[left]