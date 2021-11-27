class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0

        while i < len(s):

            if i + 1 < len(s) and roman_to_num[s[i]] < roman_to_num[s[i + 1]]:
                total += roman_to_num[s[i + 1]] - roman_to_num[s[i]]
                i += 2

            else:
                total += roman_to_num[s[i]]
                i += 1

        return total


s = "III"
s = "MCMXCIV"
print(Solution().romanToInt(s))
