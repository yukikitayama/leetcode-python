class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            # When current character is closing
            if char in close_to_open:

                # Pop from the top of the stack, pop() is pop from the last by default
                top = stack.pop() if stack else '#'
                if close_to_open[char] != top:
                    return False
            # When current character is opening
            else:
                # Add it to top of the stack
                stack.append(char)

        # If stack is empty, not stack is True
        return not stack


"""
Time complexity
Let n be the length of s, O(n) to iteral for-loop

Space complexity
In the worst case, all the characters go to stack, so O(n)
"""