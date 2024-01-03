"""
- find source row
  how many in the row
- find target row
  how many in the row
- source num * target num
"""

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        ans = 0

        prev = 0
        found_first = False

        for i, row in enumerate(bank):

            curr = sum([int(cell) for cell in row])

            if curr == 0:
                continue

            if curr > 0 and not found_first:
                prev = curr
                found_first = True

            elif prev > 0 and curr > 0:
                ans += curr * prev
                prev = curr

        return ans


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0

        for i, row in enumerate(bank):
            curr = sum([int(cell) for cell in row])

            if curr > 0:
                ans += prev * curr
                prev = curr

        return ans


if __name__ == "__main__":
    bank = ["011001", "000000", "010100", "001000"]
    bank = ["000", "111", "000"]
    print(Solution().numberOfBeams(bank))
