"""
- Use union find
  - union two nodes if they share a common factor greater than 1
"""


from typing import List
import math
import collections


class DisjointSetUnion:
    def __init__(self, size):
        # +1 because we wanna make num equal to index to parent array
        # Constraints says 1 <= nums[i], so we won't use parent[0]
        # e.g. num: 1, parent[1]
        self.parent = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            # Find parent and put the parent to this current node
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Merge two components and return the merged component ID"""
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return px

        if self.size[px] > self.size[py]:
            px, py = py, px

        self.parent[px] = py
        self.size[py] += self.size[px]
        return py


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        dsu = DisjointSetUnion(max(nums))

        for num in nums:
            for factor in range(2, int(math.sqrt(num)) + 1):
                # Remainder needs to be 0 to be a factor
                if num % factor == 0:
                    # Divisor with 0 remainder is a factor
                    dsu.union(num, factor)

                    # Also the quotient from the division is a factor
                    dsu.union(num, num // factor)

                    print(f'  dsu.union(num: {num}, factor: {factor})')
                    print(f'  dsu.union(num: {num}, num // factor: {num // factor})')
                    print(f'    dsu.parent: {dsu.parent}')
                    print(f'    dsu.size: {dsu.size}')

        print(f'dsu.parent: {dsu.parent}')
        print(f'dsu.size: {dsu.size}')

        max_size = 0
        group_count = collections.defaultdict(int)
        for num in nums:
            group_id = dsu.find(num)
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])

        print(f'group_count: {group_count}')

        return max_size


# num = 6
# factor = 2
# print(num // factor)
# print(num % factor)
nums = [4, 6, 15, 35]
print(Solution().largestComponentSize(nums))


