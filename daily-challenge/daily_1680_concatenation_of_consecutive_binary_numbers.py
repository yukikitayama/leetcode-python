class Solution:
    def concatenatedBinary(self, n: int) -> int:
        concatenated = ''.join(bin(i)[2:] for i in range(n + 1))
        return int(concatenated, 2) % (10**9 + 7)