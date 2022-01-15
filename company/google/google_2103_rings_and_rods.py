import collections


class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings) // 2

        rod_to_color = collections.defaultdict(set)

        for i in range(0, len(rings), 2):

            color = rings[i]
            rod = rings[i + 1]

            rod_to_color[rod].add(color)

        ans = 0
        for v in rod_to_color.values():
            if len(v) == 3:
                ans += 1
        return ans


"""
- Time and space O(n)
"""


if __name__ == '__main__':
    rings = "B0B6G0R6R0R6G9"
    rings = "B0R0G0R9R0B0G0"
    rings = "G4"
    print(Solution().countPoints(rings))
