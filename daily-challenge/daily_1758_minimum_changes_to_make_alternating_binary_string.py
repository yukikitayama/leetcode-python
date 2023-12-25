"""
2 passes
"""


class Solution:
    def minOperations(self, s: str) -> int:
        start_0 = 0
        start_1 = 0

        for i in range(len(s)):

            # Even index
            if i % 2 == 0:
                if s[i] == "0":
                    start_1 += 1
                else:
                    start_0 += 1

            # Odd index
            else:
                if s[i] == "0":
                    start_0 += 1
                else:
                    start_1 += 1

        return min(start_1, start_0)


if __name__ == "__main__":
    s = "0100"
    s = "10"
    s = "1111"
    print(Solution().minOperations(s))
