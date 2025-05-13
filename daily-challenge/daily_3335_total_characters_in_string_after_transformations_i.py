class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7

        counter = [0] * 26

        for c in s:
            counter[ord(c) - ord("a")] += 1

        for i in range(t):

            next_counter = [0] * 26

            # z -> a
            next_counter[0] = counter[25]

            # z -> b and a -> b
            next_counter[1] = (counter[25] + counter[0]) % mod

            # c to z
            for i in range(2, 26):
                next_counter[i] = counter[i - 1]

            counter = next_counter

        return sum(counter) % mod