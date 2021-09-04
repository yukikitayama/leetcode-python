from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        hull = []
        if len(trees) < 4:
            for tree in trees:
                hull.append(tree)
            return list(hull)

        # Find most left
        left_most = 0

        for i in range(len(trees)):
            if trees[i][0] < trees[left_most][0]:
                left_most = i

        print(f'Left most index: {left_most}, Left most tree: {trees[left_most]}')

        # Use most left as starting tree
        p = left_most

        while True:

            q = (p + 1) % len(trees)

            for i in range(len(trees)):
                if self.orientation(trees[p], trees[i], trees[q]) < 0:
                    q = i

            for i in range(len(trees)):
                if i != p and \
                    i != q and \
                    self.orientation(trees[p], trees[i], trees[q]) == 0 and \
                    self.in_between(trees[p], trees[i], trees[q]):
                    hull.append(trees[i])

            hull.append(trees[q])
            p = q

            # print(f'p: {p}, left_most: {left_most}')

            if p == left_most:
                break

        return hull

    def orientation(self, p: List[int], q: List[int], r: List[int]) -> int:
        """Inner product of pq vector and qr vector"""
        return (p[1] - p[1]) * (r[0] - p[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def in_between(self, p: List[int], i: List[int], q: List[int]) -> bool:
        # Return True is i is between p and q
        is_x_between = i[0] >= p[0] and i[0] <= q[0] or i[0] <= p[0] and i[0] >= q[0]
        is_y_between = i[1] >= p[1] and i[1] <= q[1] or i[1] <= p[1] and i[1] >= q[1]
        return is_x_between and is_y_between


trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
print(Solution().outerTrees(trees))
