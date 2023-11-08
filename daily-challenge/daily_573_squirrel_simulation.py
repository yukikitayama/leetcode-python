"""
"""

from typing import List


class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:

        def compute_distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        total_distance = 0

        maximized_saving = float("-inf")

        for nut in nuts:
            total_distance += compute_distance(nut, tree) * 2

            # Squirrel should take a nut that can maximize the saving
            # If the below difference is negative, it's not worth it to go the nut from the start position
            saving = compute_distance(nut, tree) - compute_distance(nut, squirrel)
            maximized_saving = max(saving, maximized_saving)

        return total_distance - maximized_saving


if __name__ == "__main__":
    height = 5
    width = 7
    tree = [2, 2]
    squirrel = [4, 4]
    nuts = [[3, 0], [2, 5]]
    print(Solution().minDistance(height, width, tree, squirrel, nuts))
