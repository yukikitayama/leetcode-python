from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in range(len(accounts)):
            curr = 0
            for j in range(len(accounts[0])):
                curr += accounts[i][j]
            ans = max(ans, curr)
        return ans


if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(Solution().maximumWealth(accounts))
