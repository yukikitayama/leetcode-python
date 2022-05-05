class Solution:
    def __init__(self):
        self.flag = False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        self.permute(s1, s2, 0)
        return self.flag

    def permute(self, s1, s2, l):
        if l == len(s1):
            if s2.index(s1) >= 0:
                self.flag = True

        else:
            for i in range(l, len(s1)):
                s1 = self.swap(s1, l, i)
                self.permute(s1, s2, l + 1)
                s1 = self.swap(s1, l, i)

    def swap(self, s, i0, i1):
        if i0 == i1:
            return s

        s1 = s[0:i0]
        s2 = s[i0 + 1:i1]
        s3 = s[i1 + 1:]
        return s1 + s[i1] + s2 + s[i0] + s3


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
