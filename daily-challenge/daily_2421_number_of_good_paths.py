from typing import List
import collections


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ans = n = len(vals)
        f = list(range(n))
        count = [collections.Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([max(vals[i], vals[j]), i, j] for i, j in edges)

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        for v, i, j in edges:
            fi, fj = find(i), find(j)
            cj, ci = count[fi][v], count[fj][v]
            ans += ci * cj
            f[fj] = fi
            count[fi] = collections.Counter({v: ci + cj})

        return ans


if __name__ == '__main__':
    vals = [1, 3, 2, 1, 3]
    edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
    print(Solution().numberOfGoodPaths(vals, edges))

