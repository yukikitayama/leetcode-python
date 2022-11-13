class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split(' ')
        words = [word for word in words if word != '']

        return ' '.join(words[::-1])


if __name__ == '__main__':
    s = "a good   example"
    s = "  hello world  "
    print(Solution().reverseWords(s))

    print(s.split())
