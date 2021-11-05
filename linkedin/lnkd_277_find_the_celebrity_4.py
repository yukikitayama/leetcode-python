import functools


def knows(a: int, b: int):
    return True


class Solution:
    def findCelebrity(self, n: int) -> int:

        @functools.lru_cache(maxsize=None)
        def cache_knows_result(a, b):
            return knows(a, b)

        def is_celebrity(i):
            for j in range(n):
                if i == j:
                    continue
                elif cache_knows_result(i, j) or not cache_knows_result(j, i):
                    return False
            return True

        celebrity_candidate = 0

        for i in range(1, n):

            if cache_knows_result(celebrity_candidate, i):
                celebrity_candidate = i

        if is_celebrity(celebrity_candidate):
            return celebrity_candidate
        else:
            return -1


