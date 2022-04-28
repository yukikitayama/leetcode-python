"""
- Start filling with the biggest square
"""


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # n is row,
        # m is column
        ans = n * m

        def dfs(height, moves):

            print(f'  in dfs, height: {height}, moves: {moves}')

            nonlocal ans

            # n is row
            if all(h == n for h in height):

                ans = min(ans, moves)
                return

            if moves >= ans:
                return

            min_height = min(height)

            idx = height.index(min_height)

            ridx = idx + 1

            # m is column
            while ridx < m and height[ridx] == min_height:
                ridx += 1

            # n is row
            for i in range(min(ridx - idx, n - min_height), 0, -1):

                new_height = height[:]

                for j in range(i):

                    new_height[idx + j] += i

                dfs(new_height, moves + 1)

        dfs([0] * m, 0)

        return ans


if __name__ == '__main__':
    n = 2
    m = 3
    print(Solution().tilingRectangle(n, m))
