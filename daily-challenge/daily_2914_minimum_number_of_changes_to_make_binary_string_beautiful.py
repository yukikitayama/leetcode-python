class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0

        curr = s[0]
        count = 0

        for ch in s:

            if ch == curr:
                count += 1

            else:
                # Start new sequence
                if count % 2 == 0:
                    count = 1

                # Change current character
                else:
                    count = 0
                    ans += 1

                curr = ch

        return ans