class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(p1, p2):

            # Base, insert
            if p1 < 0:
                # +1 because p2 is 0-based index
                return p2 + 1

            # Base, delete
            if p2 < 0:
                # +1 because p1 is 0-based index
                return p1 + 1

            if word1[p1] == word2[p2]:
                # No operation
                return dp(p1 - 1, p2 - 1)
            else:
                # Need operation
                return min(
                    # Replace
                    dp(p1 - 1, p2 - 1),
                    # Insert a character to word2
                    dp(p1, p2 - 1),
                    # Delete a character from word1
                    dp(p1 - 1, p2)
                ) + 1

        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance1(self, word1: str, word2: str) -> int:
        p1 = 0
        p2 = 0

        ans = 0

        while p1 < len(word1) and p2 < len(word2):

            if word1[p1] != word2[p2]:

                # Delete
                if p1 < len(word1) - 1 and word1[p1 + 1] == word2[p2]:
                    ans += 1
                    p1 += 1

                # Insert
                if p2 < len(word2) - 1 and word2[p2 + 1] == word1[p1]:
                    ans += 1
                    p2 += 1

                else:
                    # Convert
                    ans += 1
                    p1 += 1
                    p2 += 1

            elif word1[p1] == word2[p2]:
                p1 += 1
                p2 += 1

        # Delete rest of characters
        if p1 < len(word1):
            ans += len(word1) - p1

        return ans
