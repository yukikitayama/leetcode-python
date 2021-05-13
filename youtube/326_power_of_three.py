class Solution:
    def isPowerOfThree(self, n):
        if n < 1:
            return False

        while (n % 3 == 0):
            tmp = n / 3
            n = n / 3

        return n == 1


"""
n = 27
27 % 3 == 0: Ture, tmp = 27 / 3 = 9, n = 27 / 3 = 9
9 % 3 == 0: True, tmp = 9 / 3 = 3, n = 9 / 3 = 3
3 % 3 == 0: True, tmp = 3 / 3 = 1, n = 3 / 3 = 1
1 % 3 == 0: False, break

n = 1
"""

# test_case = 27
# test_case = 9
test_case = 45

sol = Solution()
answer = sol.isPowerOfThree(n=test_case)
print(f'Answer: {answer}')