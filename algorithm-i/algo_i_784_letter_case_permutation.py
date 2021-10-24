from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        ans = [[]]

        for char in s:
            n = len(ans)

            print(f'char: {char}, n: {n}, ans: {ans}')

            if char.isalpha():
                for i in range(n):
                    # Copy the string that ans currently has
                    ans.append(ans[i][:])

                    # Add a new character to the original
                    ans[i].append(char.lower())
                    # Add a new but different case character to the copy
                    ans[n + i].append(char.upper())

            # If the current char is not alphabet, but digit, no need to transform it
            # so append it to all the current strings in ans list
            else:
                for i in range(n):
                    ans[i].append(char)

        return list(map(''.join, ans))


s = "a1b2"
print(Solution().letterCasePermutation(s))
