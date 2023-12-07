from typing import List
import collections


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(candidates)
        # Data structure to avoid duplicated combination
        # [(number, count)] and access by list index
        counter = [(number, counter[number]) for number in counter]

        ans = []

        def backtracking(curr, remain, list_index):

            if remain == 0:
                ans.append(curr[:])

            if remain < 0:
                return

            # Algorithm to avoid duplicated combination
            for i in range(list_index, len(counter)):

                number, count = counter[i]

                if count > 0:
                    curr.append(number)
                    # Algorithm to avoid duplicated combination
                    counter[i] = (number, count - 1)

                    backtracking(curr, remain - number, i)

                    counter[i] = (number, count)
                    curr.pop()

        backtracking([], target, 0)

        return ans


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
