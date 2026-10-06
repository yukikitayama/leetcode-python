"""
while pointers are in the range
  append
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                ans.append(word1[i])
            if i < len(word2):
                ans.append(word2[i])
        return "".join(ans)


class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        ans = []
        while p1 < len(word1) or p2 < len(word2):

            if p1 < len(word1):
                ans.append(word1[p1])
                p1 += 1

            if p2 < len(word2):
                ans.append(word2[p2])
                p2 += 1

        return "".join(ans)


class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        ans = []
        while p1 < len(word1) and p2 < len(word2):

            ans.append(word1[p1])
            p1 += 1
            if p1 == len(word1):
                break

            ans.append(word2[p2])
            p2 += 1
            if p2 == len(word2):
                break

        if p1 < len(word1):
            for i in range(p1, len(word1)):
                ans.append(word1[p1])
        if p2 < len(word2):
            for i in range(p2, len(word2)):
                ans.append(word2[p2])

        return "".join(ans)