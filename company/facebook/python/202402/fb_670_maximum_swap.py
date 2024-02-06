class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [digit for digit in str(num)]

        ans = num

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                curr = digits[:]

                curr[i], curr[j] = curr[j], curr[i]

                ans = max(ans, int("".join(curr)))

        return ans
