class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and char == stack[-1]:
                # By default, pop index is -1, so the last element
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


# s = "abbaca"
s = "azxxzy"
print(Solution().removeDuplicates(s))
