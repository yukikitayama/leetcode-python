import math


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        dictionary = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1

        for i in range(base, base * 10):

            s = str(i)
            s += s[::-1][skip:]

            palindromic_integer = int(s)

            if palindromic_integer % k == 0:
                sorted_s = "".join(sorted(s))
                dictionary.add(sorted_s)

        print(dictionary)

        fac = [math.factorial(i) for i in range(n + 1)]

        ans = 0
        for s in dictionary:

            cnt = [0] * 10

            for c in s:
                cnt[int(c)] += 1

            tot = (n - cnt[0]) * fac[n - 1]

            for x in cnt:
                tot //= fac[x]

            ans += tot

        return ans