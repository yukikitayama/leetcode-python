from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans = 1

        s = set()

        for roll in rolls:
            s.add(roll)

            # When we see all the k sides, we clear set
            # It means that next sequence length should be incremented
            # from the next number we restart collecting unique numbers
            if len(s) == k:

                ans += 1
                # Remove all items from set
                s.clear()

            # print(f"roll: {roll}, s: {s}, ans: {ans}")

        return ans