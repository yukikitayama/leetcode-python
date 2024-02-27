class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isPalindrome1(self, s: str) -> bool:
        collected = []

        for i in range(len(s)):

            if s[i].isalnum():
                collected.append(s[i].lower())

        left = 0
        right = len(collected) - 1
        while left < right:
            if collected[left] != collected[right]:
                return False
            left += 1
            right -= 1

        return True
