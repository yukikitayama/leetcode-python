from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        while sum(tickets) > 0:
            for i in range(len(tickets)):

                if tickets[i] == 0:
                    continue

                ans += 1
                tickets[i] -= 1

                if tickets[k] == 0:
                    return ans


# 6
tickets = [2,3,2]
k = 2
# 8
# tickets = [5,1,1,1]
# k = 0
print(Solution().timeRequiredToBuy(tickets, k))




