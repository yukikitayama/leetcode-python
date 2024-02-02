"""

"""

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        ans = []

        digits = "123456789"

        for length in range(len(str(low)), len(str(high)) + 1):

            for i in range(len(digits) - length + 1):

                num = int(digits[i:i + length])

                if low <= num <= high:

                    ans.append(num)

        return ans


if __name__ == "__main__":
    low = 100
    high = 300
    low = 1000
    high = 13000
    print(Solution().sequentialDigits(low, high))

