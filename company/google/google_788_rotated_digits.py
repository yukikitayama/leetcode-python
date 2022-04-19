class Solution:
    def rotatedDigits(self, n: int) -> int:
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 6, 9, 2, 5])

        def is_good(x):
            # for i in str(x) because if x = 12,
            # we need to check 1 and 2 digits in 12 for each
            s = set([int(i) for i in str(x)])
            # s set needs to be flippable by s2, but the set should not be only same flip set
            # we need to have at least one digit in s which will be different number
            return s.issubset(s2) and not s.issubset(s1)

        ans = 0
        # It's fine to start from 0, because it will be false anyway all the times
        for i in range(n + 1):
            ans += is_good(i)

            # print(f'i: {i}, is_good(i): {is_good(i)}')

        return ans


if __name__ == '__main__':
    n = 10
    print(Solution().rotatedDigits(n))
