from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # Key: team character, value: score for each rank for each team
        # +[v] because when we have tie, we need to rank them alphabetically
        # We need to record all the ranks for all the team for handling ties
        count = {v: [0] * len(votes[0]) + [v] for v in votes[0]}

        # print(count)

        for vote in votes:

            for i, v in enumerate(vote):

                # Record team v's ith rank
                # By decrementing, more negative, stronger team, in sorting at the end
                count[v][i] -= 1

        # print(count)

        return ''.join(sorted(votes[0], key=count.get))


if __name__ == '__main__':
    votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
    # ACB
    votes = ["WXYZ", "XYZW"]
    # XWYZ
    print(Solution().rankTeams(votes))
