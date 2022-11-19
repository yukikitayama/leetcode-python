from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees = sorted(trees, key=lambda x: (x[0], x[1]))

        if len(trees) <= 1:
            return trees

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        lower = []
        for tree in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], tree) < 0:
                lower.pop()
            lower.append(tree)

        upper = []
        for tree in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], tree) < 0:
                upper.pop()
            upper.append(tree)

        tmp = set()
        for tree in lower[:-1] + upper[:-1]:
            tmp.add((tree[0], tree[1]))
        return list([[t[0], t[1]] for t in tmp])


if __name__ == '__main__':
    trees = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
    print(Solution().outerTrees(trees))

