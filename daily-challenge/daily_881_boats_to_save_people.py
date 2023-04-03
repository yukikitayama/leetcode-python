from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        ans = 0

        people.sort()

        i = 0
        j = len(people) - 1

        while i <= j:

            ans += 1

            # No while loop because a boat can carry at most 2 people
            # Once we know current light person can match with heavy person, move on
            if people[i] + people[j] <= limit:
                i += 1

            j -= 1

        return ans


