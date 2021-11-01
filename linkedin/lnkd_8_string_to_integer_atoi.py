class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        ls = list(s.strip())

        if len(ls) == 0:
            return 0

        print(f'ls: {ls}')

        sign = -1 if ls[0] == '-' else 1

        if ls[0] in ['-', '+']:
            del ls[0]

        print(f'ls: {ls}')

        ans = 0
        i = 0

        # If the current character is not digit,
        # ignore the rest of the characters
        while i < len(ls) and ls[i].isdigit():
            ans = ans * 10 + int(ls[i])
            i += 1

        # Put ans in upper range
        # If ans is beyond 2*31-1, overwrite here
        ans = min(sign * ans, 2**31-1)

        # Put ans in lower range
        # If ans is beyond -2**31-1, overwrite here
        ans = max(ans, -2*31)

        return ans



s = "42"
s = '-42'
print(Solution().myAtoi(s))

