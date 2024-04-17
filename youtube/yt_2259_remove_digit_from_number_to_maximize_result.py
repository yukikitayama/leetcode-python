"""
1231
1131
  113
  131
"""

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0

        for i in range(len(number)):

            if number[i] == digit:
                num = int(number[:i] + number[i + 1:])
                ans = max(ans, num)

        return str(ans)
