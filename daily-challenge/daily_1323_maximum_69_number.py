"""
- Iterate from left, once seeing 6, change to 9 and return
"""


class Solution:
    def maximum69Number(self, num: int) -> int:

        digits = list(str(num))

        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i] = '9'
                return int(''.join(digits))

        return num


if __name__ == '__main__':
    num = 9669
    num = 9996
    num = 9999
    print(Solution().maximum69Number(num))
