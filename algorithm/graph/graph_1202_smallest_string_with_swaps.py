"""
Result
- Start: 2:14
- End: 2:20

Idea
- If pairs is [[0, 1], [0, 2]], 0 and 1 are exchangeable, and 0 and 2 are exchangeable,
  so any 2 in (0, 1, 2) are exchangeable.
- For each connected component, find a lexicographically smallest order of characters
- Iterate each index in s
  - From the index, find root node index by object union find, and find the currently smallest character
"""


from typing import List
import collections


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for x, y in pairs:
            uf.union(x, y)

        print(f'uf.root: {uf.root}')

        # m is hashmap with key root node in union find and value lists of characters
        # Make a sorted list of characters for each connected component
        # sorted in terms of index in s
        m = collections.defaultdict(list)
        for i in range(len(s)):
            m[uf.find(i)].append(s[i])

        print(f'm: {m}')

        # Sort characters within the same connected component
        # Sort by descending order, because at below pop a character from the end of each list
        for comp_id in m.keys():
            print(f'comp_id: {comp_id}')
            m[comp_id].sort(reverse=True)

        # For each index, get the smallest character in each connected component to make answer string
        ans = []
        for i in range(len(s)):
            ans.append(m[uf.find(i)].pop())

        print(f'ans: {ans}')

        return ''.join(ans)


s = "dcab"
pairs = [[0,3],[1,2]]
print(Solution().smallestStringWithSwaps(s, pairs))


