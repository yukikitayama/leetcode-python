class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # DP array starts at 0, and ends at n,
        # so to make that array, length is n + 1, otherwise, one more thing is missing
        # This is also because at the end, we wanna access by n by cache[n]
        # Without appending one more length, it will be index out of range
        # when n = 3, cache: [0, 0, 0, 0]
        # cache[2]: cache[1] + cache[2]
        # cache[3]: cache[2] + cache[1]
        cache = [0] * (n + 1)
        # No need for index 0 because it's initialized with 0
        # but fibonacci one is one, so manually initialize with 1
        cache[1] = 1

        # +1 because range end is exclusive
        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]
