from typing import List
import collections


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Key: remainder, value: number of item in time which makes the remainder by % 60
        remainders = collections.defaultdict(int)
        ans = 0

        for t in time:

            # if a % 60 == 0, a % 60 == 0 and b % 60 == 0
            if t % 60 == 0:
                ans += remainders[0]

            # if a % 60 == 0, a % 60 + b % 60 == 60
            # b % 60 = 60 - a % 60
            else:
                ans += remainders[60 - t % 60]

            remainders[t % 60] += 1

        return ans


"""
- Time is O(N)
- Space is O(1) because remainder ranges from 0 to 59
"""


class Solution1:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    ans += 1
        return ans


"""
- Time is O(N^2)
"""


if __name__ == '__main__':
    time = [30, 20, 150, 100, 40]
    print(Solution().numPairsDivisibleBy60(time))