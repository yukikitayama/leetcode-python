class Solution:
    def confusingNumber(self, n: int) -> bool:

        digits = [d for d in str(n)]
        reversed_digits = []

        for digit in digits[::-1]:

            if digit in ['2', '3', '4', '5', '7']:
                return False

            elif digit == '6':
                reversed_digits.append('9')

            elif digit == '9':
                reversed_digits.append('6')

            else:
                reversed_digits.append(digit)

        if digits == reversed_digits:
            return False

        return True


if __name__ == '__main__':
    n = 89
    # n = 11
    # n = 6
    print(Solution().confusingNumber(n))
