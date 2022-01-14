class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # Ignore leading spaces
        while index < n and s[index] == ' ':
            index += 1

        # Check sign
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1

        # Traverse digits and stop if it's not a digit
        while index < n and s[index].isdigit():

            digit = int(s[index])

            # Check overflow and underflow
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = 10 * result + digit
            index += 1

        return sign * result


if __name__ == '__main__':
    s = '42'
    s = "   -42"
    s = "4193 with words"
    print(Solution().myAtoi(s))
