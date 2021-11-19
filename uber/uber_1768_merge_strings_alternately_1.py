class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0

        ans = []

        while p1 < len(word1) and p2 < len(word2):
            ans.append(word1[p1])
            p1 += 1
            ans.append(word2[p2])
            p2 += 1

        ans = ''.join(ans)

        if p1 < len(word1):
            ans += word1[p1:]
        elif p2 < len(word2):
            ans += word2[p2:]

        return ans


"""
Complexity
- Time is O(max(n, m)) by n length word1 and m length word2
- Space is O(max(n, m))
"""


word1 = "abc"
word2 = "pqr"
# "apbqcr"
word1 = "ab"
word2 = "pqrs"
# "apbqrs"
print(Solution().mergeAlternately(word1, word2))


