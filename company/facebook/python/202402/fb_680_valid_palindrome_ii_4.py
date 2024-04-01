class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        deleted = False
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if check_palindrome(left + 1, right) or check_palindrome(left, right - 1):
                    return True
                else:
                    return False

        return True