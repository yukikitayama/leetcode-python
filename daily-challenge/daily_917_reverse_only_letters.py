class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Extract only alphabet and make a list
        # But here letters is a stack meant to be popped from the last element to reverse
        letters = [c for c in s if c.isalpha()]
        # print(letters)
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)


"""
Time complexity
Let n be the length of s. O(n) for for-loop

Space complexity
O(n) for stack
"""


s = "ab-cd"
print(Solution().reverseOnlyLetters(s))
