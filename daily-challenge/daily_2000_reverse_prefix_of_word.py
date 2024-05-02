class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = []

        found = False
        for i in range(len(word)):

            ans.append(word[i])

            if word[i] == ch and not found:
                ans.reverse()
                found = True

        return "".join(ans)