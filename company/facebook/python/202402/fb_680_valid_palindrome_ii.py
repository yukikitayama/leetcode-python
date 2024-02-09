class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Delete left
                res_left = is_palindrome(left + 1, right)
                # Delete right
                res_right = is_palindrome(left, right - 1)
                return res_left or res_right

        return True


if __name__ == "__main__":
    s = "aba"
    s = "abca"
    s = "abc"
    print(Solution().validPalindrome(s))