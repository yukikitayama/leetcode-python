from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def generate_sieve_array(upper):
            sieve = [True] * (upper + 1)
            # 0 and 1 are not prime number
            sieve[0] = sieve[1] = False

            for number in range(2, int(upper ** 0.5) + 1):
                if sieve[number]:
                    for multiple in range(number * number, upper + 1, number):
                        sieve[multiple] = False

            return sieve

        sieve_array = generate_sieve_array(right)

        prime_numbers = [num for num in range(left, right + 1) if sieve_array[num]]

        if len(prime_numbers) < 2:
            return [-1, -1]

        min_so_far = float("inf")
        ans = [None, None]
        for i in range(1, len(prime_numbers)):
            diff = prime_numbers[i] - prime_numbers[i - 1]
            if diff < min_so_far:
                ans[0] = prime_numbers[i - 1]
                ans[1] = prime_numbers[i]
                min_so_far = diff

        return ans