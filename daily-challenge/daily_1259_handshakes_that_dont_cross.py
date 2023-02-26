import functools


class Solution:
    @functools.lru_cache(maxsize=None)
    def numberOfWays(self, numPeople):
        return sum(self.numberOfWays(i) * self.numberOfWays(numPeople - 2 - i) for i in range(0, numPeople, 2)) % (10**9 + 7) if numPeople else 1

