class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ''

        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                palindrome = palindrome[:i] + 'a' + palindrome[i + 1:]
                return palindrome

        palindrome = palindrome[:len(palindrome) - 1] + 'b'
        return palindrome


palindrome = "abccba"
print(Solution().breakPalindrome(palindrome))
