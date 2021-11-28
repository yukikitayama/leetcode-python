from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # n = len(piles)
        # print(f'piles: {piles}')
        # for i in range(n - 2, -1, -1):
        #     piles[i] += piles[i + 1]
        # print(f'prefix sum from end: {piles}')

        # print(f'piles: {piles}')
        # _suffix_sum() gives us the prefix sum from the end and 0 is appended at the right end
        suffix_sum = self._suffix_sum(piles)
        # print(f'suffix_sum: {suffix_sum}')

        @lru_cache(maxsize=None)
        def dfs(pile, M, turn):
            """turn is True when Alice, and False when Bob"""
            sum_alice, sum_bob = suffix_sum[pile], suffix_sum[pile]

            # print(f'sum_alice: {sum_alice}, sum_bob: {sum_bob}')

            # range() comes from 1 <= X <= 2M in problem.
            # +1 to both arguments in min() because suffix_sum is 1 length longer than piles
            # by appending 0 at the right end
            for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                sum_alice_next, sum_bob_next = dfs(next_pile, max(M, next_pile - pile), not turn)

                range_sum = suffix_sum[pile] - suffix_sum[next_pile]

                # Alice
                if turn:
                    if sum_bob_next < sum_bob:
                        sum_alice = sum_alice_next + range_sum
                        sum_bob = sum_bob_next
                else:
                    if sum_alice_next < sum_alice:
                        sum_alice = sum_alice_next
                        sum_bob = sum_bob_next + range_sum

            return sum_alice, sum_bob

        return dfs(0, 1, True)[0]

    def _suffix_sum(self, piles: List[int]) -> List[int]:
        suffix_sum = [0]

        for pile in reversed(piles):
            suffix_sum.append(suffix_sum[-1] + pile)

        suffix_sum.reverse()

        return suffix_sum




piles = [2, 7, 9, 4, 4]
print(Solution().stoneGameII(piles))
