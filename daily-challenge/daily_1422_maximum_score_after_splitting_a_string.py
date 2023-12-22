"""
Left scan, right scan
"""


class Solution:
    def maxScore(self, s: str) -> int:

        ans = float("-inf")

        for i in range(len(s) - 1):

            left = s[:(i + 1)]
            right = s[(i + 1):]

            count_zero = left.count("0")
            count_one = right.count("1")

            ans = max(ans, count_zero + count_one)

        return ans


class SolutionTwoPass:
    def maxScore(self, s: str) -> int:
        ans = float("-inf")

        count_one = s.count("1")
        count_zero = 0

        for i in range(len(s) - 1):

            if s[i] == "1":
                count_one -= 1

            elif s[i] == "0":
                count_zero += 1

            ans = max(ans, count_one + count_zero)

        return ans


if __name__ == "__main__":
    s = "011101"
    s = "00111"
    s = "1111"
    # s = "00"
    print(Solution().maxScore(s))
