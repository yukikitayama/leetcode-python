from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1] * len(ratings)

        for i in range(1, len(ratings)):

            if ratings[i - 1] < ratings[i]:
                # +ans[i] because more candies than the number of candies that the neighbor has
                ans[i] = max(1 + ans[i - 1], ans[i])

        for i in range(len(ratings) - 2, -1, -1):

            if ratings[i] > ratings[i + 1]:
                ans[i] = max(1 + ans[i + 1], ans[i])

        # print(f'ans: {ans}')

        return sum(ans)


if __name__ == '__main__':
    ratings = [1, 0, 2]
    # 5
    ratings = [1, 2, 2]
    # 4
    print(Solution().candy(ratings))
