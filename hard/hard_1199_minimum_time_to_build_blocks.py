from typing import List
import functools


class Solution:
    def minBuildTime1(self, blocks, split):
        n = len(blocks)

        # Sort the blocks in descending order
        blocks.sort(reverse=True)

        # dp[i][j] represents the minimum time taken to
        # build blocks[i~n-1] block using j workers
        dp = [[-1] * (n + 1) for _ in range(n)]

        def solve(b, w):
            # Base cases
            if b == n:
                return 0
            if w == 0:
                return float('inf')
            if w >= n - b:
                return blocks[b]

            # If the sub-problem is already solved, return the result
            if dp[b][w] != -1:
                return dp[b][w]

            # Two Choices
            work_here = max(blocks[b], solve(b + 1, w - 1))
            split_here = split + solve(b, min(2 * w, n - b))

            # Store the result in the dp array
            dp[b][w] = min(work_here, split_here)
            return dp[b][w]

        # For block from index 0, with 1 worker
        return solve(0, 1)

    def minBuildTime(self, blocks: List[int], split: int) -> int:
        blocks.sort(reverse=True)

        @functools.lru_cache(maxsize=None)
        def dp(b, w):
            """
            b: index to blocks array
            w: current number of workers
            """

            # Base case: built all the blocks so no more cost
            if b == len(blocks):
                return 0

            # Base case: worker isn't available, return inf as impossible, but this will be fixed by min()
            if w == 0:
                return float("inf")

            # Base case: too many worker, so no need to split, greedily build current block
            if w >= len(blocks) - b:
                return blocks[b]

            # max() because build and next task happen in parallel
            work = max(blocks[b], dp(b + 1, w - 1))
            s = split + dp(b, min(2 * w, len(blocks) - b))

            return min(work, s)

        return dp(0, 1)