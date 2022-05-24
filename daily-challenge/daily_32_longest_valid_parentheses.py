class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        # Initialize having -1 because we wanna calculate length of substring
        # by current index - (before start index)
        stack = [-1]

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)

                else:
                    ans = max(ans, i - stack[-1])

        return ans


if __name__ == '__main__':
    s = "(()"
    s = ")()())"
    print(Solution().longestValidParentheses(s))
