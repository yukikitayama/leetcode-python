"""
Let n denote the number of couples
Answer is n - the number of connected components in the initial row data
"""

from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:

        # Number of couples
        n = len(row) // 2

        # Couples array represents where each person sits in the initial row
        # [[0, 1], ...] means left person (even num person) of couple ID 1 sits at the first seat,
        # and right person (odd num person) of couple ID 1 sits at the second seat.
        couples = [[] for _ in range(n)]
        for i, person in enumerate(row):
            couple_id = person // 2
            curr_seat_id = i // 2
            couples[couple_id].append(curr_seat_id)

        print(couples)

        adj = [[] for _ in range(n)]
        for x, y in couples:
            adj[x].append(y)
            adj[y].append(x)

        print(adj)

        ans = n

        for start in range(n):

            print(f"start: {start}")

            if not adj[start]:
                continue

            ans -= 1

            x = start
            y = adj[start].pop()

            print(f"  x: {x}, y: {y}")

            while y != start:
                adj[y].remove(x)
                x, y = y, adj[y].pop()

            print(f"  adj: {adj}, ans: {ans}")

        return ans

    def minSwapsCouples1(self, row: List[int]) -> int:
        """TLE"""

        # Number of couples
        n = len(row) // 2

        # Assign couple ID for each person
        # Couple shares the same couple ID
        pairs = [[row[i] // 2, row[i + 1] // 2] for i in range(0, 2 * n, 2) if row[i] // 2 != row[i + 1] // 2]

        print(pairs)

        def swap(c1, p1, c2, p2):
            pairs[c1][p1], pairs[c2][p2] = pairs[c2][p2], pairs[c1][p1]

        def solve(index):

            # Terminate
            if index == len(pairs):
                return 0

            c_l, c_r = pairs[index]

            # They are already sitting together
            if c_l == c_r:
                # Go to the next couple seat
                return solve(index + 1)

            # If they are not couple
            # Find another couple seat
            for c in range(index + 1, len(pairs)):

                # Try both people in the couple seat
                for p in [0, 1]:

                    # If this persons has the same couple ID as current left person
                    if pairs[c][p] == c_l:
                        other_index_r = c
                        other_person_r = p

                    # If this persons has the same couple ID as current right person
                    if pairs[c][p] == c_r:
                        other_index_l = c
                        other_person_l = p

            # Try swapping person at the right
            swap(index, 1, other_index_r, other_person_r)
            res1 = 1 + solve(index + 1)

            # Backtrack
            swap(index, 1, other_index_r, other_person_r)

            # Try swapping person at the left
            swap(index, 0, other_index_l, other_person_l)
            res2 = 1 + solve(index + 1)

            # Backtrack
            swap(index, 0, other_index_l, other_person_l)

            # Minimize
            return min(res1, res2)

        return solve(0)