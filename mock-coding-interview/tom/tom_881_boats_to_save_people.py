from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        ans = 0

        left = 0
        right = len(people) - 1

        while left <= right:

            # We always send heaviest person
            # But if lightest person can join the same ship, we add the lightest person
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1

        return ans