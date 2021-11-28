import sys
print(sys.getrecursionlimit())
# sys.setrecursionlimit(100000)


class Solution:
    def __init__(self):
        self.count = 0
        self.modulo = 10**9 + 7

    def checkRecord(self, n: int) -> int:
        self.gen('', n)
        return self.count

    def gen(self, s, n):
        # print(f's: {s}')

        # When n is 0, recursively made s becomes length n
        # Becuase we append another character when we decrement n in elif block
        # So when s length is the required length and check_validity says s is eligible for the award,
        # we count up
        if n == 0 and self.check_validity(s):
            self.count = (self.count + 1) % self.modulo
        elif n > 0:
            self.gen(s + 'A', n - 1)
            self.gen(s + 'P', n - 1)
            self.gen(s + 'L', n - 1)

    def check_validity(self, s):
        num_A = 0
        for i in range(len(s)):
            # Why c < 2? => Just to make it a bit faster by reducing unnecessary loops
            # if s[i] == 'A' and c < 2:
            if s[i] == 'A':
                num_A += 1

        # len(s) > 0
        # c < 2: A needs to be less than 2 in total
        # s.find('LLL') < 0: No late for 3 or more consecutive days
        # print(f'check_validity({s}): {len(s) > 0 and c < 2 and s.find("LLL") < 0} for '
        #       f'len(s) > 0: {len(s) > 0}, c < 2: {c < 2}, s.find("LLL") < 0: {s.find("LLL") < 0}')
        return len(s) > 0 and num_A < 2 and s.find('LLL') < 0


# print(Solution().checkRecord(2))
# print(Solution().checkRecord(1))
# print(Solution().checkRecord(10101))
print(Solution().checkRecord(3))
# print(Solution().checkRecord(4))
