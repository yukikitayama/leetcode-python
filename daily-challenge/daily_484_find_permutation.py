"""
- Start with ascending integers
- Reverse the ordered integers only where D
- Use stack
  - Push to stack when D
  - Pop from stack when I
"""


from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        # +1 because s represent delta between 2
        ans = [None] * (len(s) + 1)
        stack = []

        j = 0

        for i in range(1, len(s) + 1):

            # print(f'i: {i}')

            if s[i - 1] == 'I':
                stack.append(i)

                while stack:
                    ans[j] = stack.pop()
                    j += 1

            else:
                stack.append(i)

        # print(f'ans: {ans}, stack: {stack}')

        stack.append(len(s) + 1)
        while stack:
            ans[j] = stack.pop()
            j += 1

        return ans


if __name__ == '__main__':
    s = 'DI'
    print(Solution().findPermutation(s))
