"""

"""


import collections


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def is_numerically_balanced(num):
            count = collections.Counter(str(num))

            for key, value in count.items():
                if int(key) != value:
                    return False

            return True

        # print('22', is_numerically_balanced(22))
        # print('1333', is_numerically_balanced(1333))
        # print('3133', is_numerically_balanced(3133))

        for i in range(n + 1, 1000000000):
            if is_numerically_balanced(i):
                return i


n = 1
n = 1000
# n = 3000
print(Solution().nextBeautifulNumber(n))
