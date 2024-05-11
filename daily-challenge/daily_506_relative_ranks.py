from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_to_index = [None] * (1 + max(score))
        for i in range(len(score)):
            score_to_index[score[i]] = i

        ans = [None] * len(score)
        rank = 1
        for i in range(len(score_to_index) - 1, -1, -1):

            if score_to_index[i] is not None:

                rank_output = str(rank)
                if rank == 1:
                    rank_output = "Gold Medal"
                elif rank == 2:
                    rank_output = "Silver Medal"
                elif rank == 3:
                    rank_output = "Bronze Medal"

                ans[score_to_index[i]] = rank_output
                rank += 1

        return ans

    def findRelativeRanks1(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        ranking = {}
        for i in range(len(sorted_score)):
            ranking[sorted_score[i]] = i + 1

        ans = []

        for i in range(len(score)):
            rank = ranking[score[i]]

            if rank == 1:
                ans.append("Gold Medal")
            elif rank == 2:
                ans.append("Silver Medal")
            elif rank == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank))

        return ans
