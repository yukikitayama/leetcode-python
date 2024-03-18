class Solution:
    def reverseWords(self, s: str) -> str:

        left = 0
        right = len(s) - 1

        while left < right and s[left] == " ":
            left += 1

        while left < right and s[right] == " ":
            right -= 1

        stack = []
        word = []

        # print(left, right)

        # <= for the last word to contain all the characters
        while left <= right:

            if word and s[left] == " ":
                stack.append("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1

        # Last word
        stack.append("".join(word))

        # print(stack)

        stack.reverse()

        return " ".join(stack)

    def reverseWords1(self, s: str) -> str:
        words = s.split(" ")

        ans = []

        for i in range(len(words) - 1, -1, -1):

            if words[i] != "":
                ans.append(words[i])

        return " ".join(ans)