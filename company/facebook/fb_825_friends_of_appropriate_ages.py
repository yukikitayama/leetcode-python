"""
- Make a graph, bidirectional
  - Implement request condition in iteration
- Count edges
- T: O(N), S: O(N)

- collections.Counter
"""


from typing import List
import collections


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = collections.Counter(ages)

        # print(c)

        def count_request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or (b > 100 and a < 100))

        # It looks like O(N^2), but constrains says 1 <= age <= 120 (<- N)
        ans = 0
        for a in c:
            for b in c:
                # print(f'a: {a}, b: {b}')
                # Count bidirectional but remove the request to themself
                ans += count_request(a, b) * (c[a] * (c[b] - (a == b)))

        return ans


if __name__ == '__main__':
    ages = [16, 17, 18]
    # print(0.5 * 16 + 7)
    # print(0.5 * 17 + 7)
    # print(0.5 * 18 + 7)
    # 18 won't send request to 16 because 0.5 * 18 + 7 = 16
    ages = [20, 30, 100, 110, 120]
    print(Solution().numFriendRequests(ages))
