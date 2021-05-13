from math import sqrt


class Solution:
    def countPrimes(self, n):
        # 2 is a prime number but we return prime numbers less than n so <= 2
        if n <= 2:
            return 0

        # This dictionary contains non-prime numbers
        numbers = {}

        print(f'sqrt(n): {sqrt(n):.1f}')

        # We have non-prime by getting the multiples of the primes until n
        # So we start from smallest prime 2 to sqrt(n) + 1, because we do p*p below, and +1 for inclusive
        for p in range(2, int(sqrt(n)) + 1):

            # Check the primes which we have not checked
            if p not in numbers:

                print(f'Prime: {p}')

                # range(start, stop, step)
                # Make non-primes by the multiples of the primes
                for multiple in range(p * p, n, p):

                    # Save non-primes
                    numbers[multiple] = 1
                    print(f'Non-prime: {multiple}')

        print(f'All the non-primes: {numbers}')

        # Get number of prime numbers by available numbers minus non-prime numbers in numbers dictionary and minus 0 and
        # 1, because we started from 2 but they are in the original available numbers.
        # When exclusive n = 10, available numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numbers: {4: 1, 6: 1, 8: 1, 9: 1},
        # len(numbers): 4
        # 10 - 4 = 6 -> [0, 1, 2, 3, 5, 7]
        # 6 - 2 = 4 -> [2, 3, 5, 7]
        return n - len(numbers) - 2


def main():

    # Test
    test_case = 10
    sol = Solution()
    answer = sol.countPrimes(n=test_case)
    print(f'Answer: {answer}')


if __name__ == '__main__':
    main()
