class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for length_N in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length_N
        return -1


if __name__ == '__main__':
    n = 1
    k = 1
    n = 111
    k = 3
    # print(f'n: {n} is divisible by k: {n % k == 0}, n / k: {n / k}')

    remainder = 1
    length_N = 1
    # K = 1
    # K = 2
    K = 3
    print(f'K: {K}, remainder: {remainder}, length_N: {length_N}')
    print()

    print(f'remainder % K: {remainder % K}')
    N = remainder * 10 + 1
    print(f'N: {N}')
    # Because of N % K, remainder is only ranging from 0 to K-1
    remainder = N % K
    print(f'remainder: {remainder}')
    length_N += 1
    print(f'length_N: {length_N}')
    print()

    print(f'remainder % K: {remainder % K}')
    N = remainder * 10 + 1
    print(f'N: {N}')
    remainder = N % K
    print(f'remainder: {remainder}')
    length_N += 1
    print(f'length_N: {length_N}')
    print()

    print(f'remainder % K: {remainder % K}')
    N = remainder * 10 + 1
    print(f'N: {N}')
    remainder = N % K
    print(f'remainder: {remainder}')
    length_N += 1
    print(f'length_N: {length_N}')
    print()
