"""
1: 0
- Length: 2^0 = 1
2: 01
- Length: 2^1 = 2
3: 0110 (0 -> 01, 1 -> 10)
- Length: 2^2 = 4
4: 01101001
- Length: 2^3 = 8

- First half is the same as n - 1
- Second half is the complement of the first half
- Length at n is 2^(n - 1)
- If k is in first half, same as kth item in n - 1
- If k is in second half, the complement
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        print(f'n: {n}, k: {k}')

        # Base case
        if n == 1:
            if k == 1:
                return 0
            else:
                return 1

        # half is the length at n
        # e.g. n: 3, half: 4, str: 0110
        # e.g. n: 4, half: 8, str: 01101001
        half = 2 ** (n - 1)

        print(f'  half: {half}, k - half: {k - half}')

        # If k is smaller than or equal to half, k is the first half
        # otherwise k is the second half
        if k <= half:
            return self.kthGrammar(n - 1, k)
        else:
            res = self.kthGrammar(n - 1, k - half)
            # It needs to be complement, so if res is 0, answer is 1
            if res == 0:
                return 1
            else:
                return 0


if __name__ == '__main__':
    # n = 2
    # n = 3
    n = 4
    # k = 1
    k = 3
    print(Solution().kthGrammar(n, k))
    # print(Solution().kthGrammar(1, 1))
    # print(Solution().kthGrammar(2, 1))
    # print(Solution().kthGrammar(2, 2))

