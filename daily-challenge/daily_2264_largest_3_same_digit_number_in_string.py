"""
check if current 3 letters is equal to first letter multiplied by 3 times
compare string numbers by operators to find max
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""

        for i in range(len(num) - 2):

            curr = num[i:i + 3]

            # "000" < "111": True
            # "" < "000": True
            if curr == curr[0] * 3 and curr > ans:
                ans = curr

        return ans


if __name__ == "__main__":
    num = "6777133339"
    num = "2300019"
    num = "42352338"
    num = "222"
    print(Solution().largestGoodInteger(num))
