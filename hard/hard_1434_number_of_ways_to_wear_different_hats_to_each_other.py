from typing import List
import functools
import collections


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        # len(hats): 3, 3 people, 2**3: 8, bin(8): 1000, 2**3 - 1 = 7, bin(7): 111
        done = 2 ** len(hats) - 1

        hat_to_people = collections.defaultdict(list)
        for i in range(len(hats)):
            for hat in hats[i]:
                hat_to_people[hat].append(i)

        @functools.cache
        def dp(hat, mask):

            # Base case 1: Give everyont a hat
            if mask == done:
                return 1

            # Base case 2: Run out of hats, so cannot place hats to all the people
            if hat > 40:
                return 0

            # Recurrence relation 1: Skip current hat and move on to the next hat
            res = dp(hat + 1, mask)

            # Recurrence relation 2: Place current hat
            for person in hat_to_people[hat]:
                # If ith person not wear a hat yet
                if (1 << person) & mask == 0:
                    res += dp(hat + 1, mask | (1 << person))
                    res %= MOD

            return res

        # Start with the 1st hat and nobody is wearing a hat initially
        return dp(1, 0)