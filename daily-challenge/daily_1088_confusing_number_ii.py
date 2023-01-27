class Solution:
    def confusingNumberII(self, n: int) -> int:

        rotate180 = [
            [0, 0],
            [1, 1],
            [6, 9],
            [8, 8],
            [9, 6]
        ]

        ans = 0

        def dfs(num, num_rotated, unit):
            nonlocal ans

            if num != num_rotated:
                ans += 1

            for d, d_rotated in rotate180:

                if d == 0 and num == 0:
                    continue

                if num * 10 + d > n:
                    break

                dfs(num * 10 + d, d_rotated * unit + num_rotated, unit * 10)

        dfs(0, 0, 1)

        return ans




