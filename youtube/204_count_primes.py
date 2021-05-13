import math


class Solution:
    def countPrimes(self, n):
        if n <= 1:
            return 0

        non_prime = {}

        for k in range(2, int(math.sqrt(n)) + 1):
            print(k)

            # range(start, end, step)
            for i in range(k * k, n, k):
                non_prime[i] = 1

        print(non_prime)
        print(len(non_prime))

        num_non_prime = len(non_prime)
        prime = n - num_non_prime - 2
        return prime


test_case = 10
# test_case = 0
# test_case = 1
sol = Solution()
answer = sol.countPrimes(n=test_case)
print(f'Answer: {answer}')
