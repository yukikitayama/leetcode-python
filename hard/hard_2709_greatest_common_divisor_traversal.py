"""
With the goal of creating a graph that is efficient enough to construct in the time limit, let's consider adding some dummy nodes to reduce the number of edges. (?)
"""

from typing import List


class DSU:
    def __init__(self, size):
        # This will contain the common prime number
        # parent[i] means i is num in nums, and parent[i] is common prime number of num
        # +1 makes it easier to get prime number from give num
        self.parent = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)

    def find(self, x):
        return x if self.parent[x] == x else self.find(self.parent[x])

    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)

        if r_x == r_y:
            return

            # Keep bigger
        if self.rank[r_x] > self.rank[r_y]:
            r_x, r_y = r_y, r_x
        self.parent[r_x] = r_y
        self.rank[r_y] += self.rank[r_x]


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        # Edge case: Single node
        if len(nums) == 1:
            return True

        max_num = max(nums)
        n = len(nums)
        # Track which numbers we will have in the graph
        has = [False] * (max_num + 1)
        for num in nums:
            has[num] = True

        # Edge case: If we have 1 in nums, impossible to achieve at least GCD 2 for pairs
        if has[1]:
            return False

        # Sieve of Eratosthenes to generate prime numbers
        # sieve[i] represents that if i == sieve[i], prime numer
        # else if sieve[i] != 0, then i isn't prime, but sieve[i] contains the prime number to create i
        # +1 makes it easier to read sieve array
        sieve = [0] * (max_num + 1)
        for d in range(2, max_num + 1):
            # If unmarked
            if sieve[d] == 0:
                # All the multiples
                for v in range(d, max_num + 1, d):
                    sieve[v] = d

        # Create graph
        dsu = DSU(max_num + 1)
        for num in nums:
            # Save current number to temporary variable
            # because this temporary variable will be updated to the next prime number which exitst in current number
            val = num

            # print(f"num: {num}")

            while val > 1:

                prime = sieve[val]

                if dsu.find(prime) != dsu.find(num):
                    dsu.union(prime, num)

                # Get another different prime number
                # e.g. val: 30, prime: 5, val % prime: 0, val //= prime: 6, next val is 6, and next prime will be 3
                while val % prime == 0:
                    val //= prime

        # Count the number of connected components
        cnt = 0
        for num in range(2, max_num + 1):
            if has[num] and dsu.find(num) == num:
                cnt += 1

        # print(f"sieve: {sieve}")
        # print(f"dsu.parent: {dsu.parent}")
        # print(f"cnt: {cnt}")

        return cnt == 1
