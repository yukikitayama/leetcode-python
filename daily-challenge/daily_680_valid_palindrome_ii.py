class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(s, i, j):
            # Terminate when i == j
            while i < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1

            return True

        i = 0
        j = len(s) - 1

        while i < j:

            # If there's mismatch, we have one chance to delete a character
            # so this block immediately returns
            if s[i] != s[j]:
                # delete front character or rear character
                return check_palindrome(s, i + 1, j) or check_palindrome(s, i, j - 1)

            i += 1
            j -= 1

        return True


