class Solution:
    def removeVowels(self, s: str) -> str:
        ans = []

        for i in range(len(s)):
            if s[i] not in ["a", "e", "i", "o", "u"]:
                ans.append(s[i])

        return "".join(ans)