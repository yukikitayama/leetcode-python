from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0

        for p in points:

            # print(f'p: {p}')

            cmap = {}

            for q in points:

                f = p[0] - q[0]
                s = p[1] - q[1]
                distance = f**2 + s**2
                cmap[distance] = cmap.get(distance, 0) + 1

            # print(cmap)

            for distance in cmap:

                # k * (k - 1) because choose n total number to choose from and we choose r
                # no repetitions, order matters.
                # e.g. k: 3, 3 * 2 = 6, 3P2 = 3! / (3 - 2)! = (3 * 2) / 1
                # k: 4, 4 * 3 = 12, 4P2 = 4! / (4 - 2)! = (4 * 3 * 2) / (2 * 1) = 12
                # k: 5, 5P2 = 5! / (5 - 2)! = (5 * 4 * 3 * 2) / (3 * 2 * 1)
                ans += cmap[distance] * (cmap[distance] - 1)

        return ans


if __name__ == '__main__':
    points = [[0, 0], [1, 0], [2, 0]]
    print(Solution().numberOfBoomerangs(points))
