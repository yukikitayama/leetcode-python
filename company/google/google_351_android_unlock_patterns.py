from collections import Counter


class Solution:
    def __init__(self):
        self.cross = Counter({
            (1, 3): 2,
            (3, 1): 2,
            (1, 7): 4,
            (7, 1): 4,
            (3, 9): 6,
            (9, 3): 6,
            (7, 9): 8,
            (9, 7): 8,
            (1, 9): 5,
            (9, 1): 5,
            (2, 8): 5,
            (8, 2): 5,
            (3, 7): 5,
            (7, 3): 5,
            (4, 6): 5,
            (6, 4): 5
        })

    def numberOfPatterns(self, m: int, n: int) -> int:
        # List to track of number used, Index: number, Value: whether it's used
        # First element is True, because 0 does not exist
        used = [True] + [False] * 9
        def dfs(i, k):
            # ?
            if not k:
                return 1

            used[i] = True
            # Try next traversal only if the followings
            # count as valid if a number does not exist in used list,
            # and the number crossed from i to j does exist in used array
            cnt = sum(dfs(j, k - 1) for j in range(1, 10) if not used[j] and used[self.cross[i,j]])
            # To do next traversal back to False
            used[i] = False
            return cnt
        # dfs(1, k) * 4 covers traverses starting from 1, 3, 7, 9 because of symmetry
        return sum(dfs(1, k) * 4 + dfs(2, k) * 4 + dfs(5, k) for k in range(m - 1, n))


