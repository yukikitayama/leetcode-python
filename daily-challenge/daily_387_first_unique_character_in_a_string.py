import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:

        counter = collections.Counter(s)

        for i, ch in enumerate(s):

            if counter[ch] == 1:
                return i

        return -1


if __name__ == '__main__':
    s = 'loveleetcode'
    print(Solution().firstUniqChar(s))
