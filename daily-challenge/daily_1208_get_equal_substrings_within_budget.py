class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0

        curr_cost = 0
        left = 0
        for right in range(len(s)):
            curr_cost += abs(ord(s[right]) - ord(t[right]))

            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            ans = max(ans, right - left + 1)

        return ans

    def equalSubstring1(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]

        print(costs)

        ans = 0

        curr_cost = 0
        left = 0
        for right in range(len(costs)):

            curr_cost += costs[right]

            while left < right and curr_cost > maxCost:
                curr_cost -= costs[left]
                left += 1

            if curr_cost <= maxCost:
                ans = max(
                    ans,
                    right - left + 1
                )

        return ans