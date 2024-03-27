from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = set()
        for i in range(len(queens)):
            queen_set.add(tuple(queens[i]))

        ans = []

        for offset_x in [-1, 0, 1]:
            for offset_y in [-1, 0, 1]:
                if offset_x == 0 and offset_y == 0:
                    continue

                for distance in range(1, 8):
                    next_x = king[0] + offset_x * distance
                    next_y = king[1] + offset_y * distance

                    if (next_x, next_y) in queen_set:
                        ans.append([next_x, next_y])
                        # Only need closest queen
                        break

        return ans
