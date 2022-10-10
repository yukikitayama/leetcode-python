class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''

        chars = [ch for ch in palindrome]

        for i in range(len(palindrome) // 2):
            if chars[i] != 'a':
                chars[i] = 'a'
                return ''.join(chars)

        chars[len(palindrome) - 1] = 'b'

        return ''.join(chars)


if __name__ == '__main__':
    palindrome = "abccba"
    palindrome = "aba"
    print(Solution().breakPalindrome(palindrome))
