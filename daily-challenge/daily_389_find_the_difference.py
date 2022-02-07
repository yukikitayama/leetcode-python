import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for ch in s:
            ans ^= ord(ch)
        for ch in t:
            ans ^= ord(ch)
        return chr(ans)


class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        c_s = collections.Counter(s)

        for ch in t:

            if ch not in c_s or c_s[ch] == 0:
                return ch

            else:
                c_s[ch] -= 1


if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    s = ""
    t = "y"
    s = 'a'
    t = 'aa'
    # a
    print(Solution().findTheDifference(s, t))

    s = 'a'
    t = 'ae'

    filter_ = 0
    for ch in s:
        filter_ ^= ord(ch)
        print(bin(ord(ch)), bin(filter_))

    for ch in t:
        filter_ ^= ord(ch)
        print(bin(ord(ch)), bin(filter_))
