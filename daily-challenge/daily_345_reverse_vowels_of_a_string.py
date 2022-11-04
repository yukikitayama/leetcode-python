class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)

        left = 0
        right = len(chars) - 1

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while left < right:

            while left < len(chars) and chars[left] not in vowels:
                left += 1

            while right >= 0 and chars[right] not in vowels:
                right -= 1

            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

            # print(f'left: {left}, right: {right}')

        return ''.join(chars)


if __name__ == '__main__':
    s = 'hello'
    print(Solution().reverseVowels(s))
