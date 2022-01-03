"""
- in degree 0 is town judge

-
"""


from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return - 1

        trusts = [0] * (n + 1)

        for t in trust:
            trusts[t[0]] -= 1
            trusts[t[1]] += 1

        # enumerate(iterable, start)
        for i, t in enumerate(trusts[1:], 1):
            if trusts[i] == n - 1:
                return i
        return -1


class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1

        in_degrees = [0] * (n + 1)
        out_degrees = [0] * (n + 1)
        for t in trust:
            in_degrees[t[1]] += 1
            out_degrees[t[0]] += 1

        print(f'in_degrees: {in_degrees}')
        print(f'out_degrees: {out_degrees}')

        for i in range(len(in_degrees)):
            if in_degrees[i] == (n - 1) and out_degrees[i] == 0:
                return i
        return -1


if __name__ == '__main__':
    n = 2
    trust = [[1, 2]]
    n = 3
    trust = [[1, 3], [2, 3]]
    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    n = 1
    trust = []
    print(Solution().findJudge(n, trust))
