from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Only sorted(cuboids) gives us a list of list where only first element of each list is ascending
        # But we want each list in the list is also ascending, so first map(sorted, cuboids) to
        # sort each list in list in ascending, and get the entire list sorted next
        cuboids = [[0, 0, 0]] + sorted(map(sorted, cuboids))

        # print(f'cuboids: {cuboids}')

        # dp[i] contains ith height
        # 0th element is a placeholder
        dp = [0] * len(cuboids)

        # print(f'dp: {dp}')

        for j in range(1, len(cuboids)):

            for i in range(j):

                # 3 because of width, length, and height
                # cuboids[i][k] is previous, cuboids[j][k] is current
                if all(cuboids[i][k] <= cuboids[j][k] for k in range(3)):

                    # 2 because 3rd element is height
                    dp[j] = max(dp[j], dp[i] + cuboids[j][2])

        # print(f'dp: {dp}')

        return max(dp)


if __name__ == '__main__':
    cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]
    # 190
    cuboids = [[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]
    # 102
    print(Solution().maxHeight(cuboids))
