import math


def sum_digits(n):
    ans = 0

    while n > 0:

        print(f'  n: {n}')

        remain = n % 10

        print(f'  remain: {remain}')

        # Increment ans by the digit from the right of n
        ans += remain

        # Remove the rightmost digit and go to the second digit from the right
        n //= 10

    return ans


n = 12  # 3
print(sum_digits(n))


print(math.log10(1))
print(math.log10(12))
print(math.log10(123))
print(math.log10(1234))
print(math.log10(12345))
print(math.log10(123456))



