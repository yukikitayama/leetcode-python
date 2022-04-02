"""
- backtracking
- pointer
"""


from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:

        ans = []

        def backtracking(s, word):
            if not s:
                ans.append(''.join(word))

            else:
                if s[0] == '{':
                    # First occurrence  index
                    i = s.find('}')
                    # 1 because 0 is '{', :i because i is exclusive
                    for letter in s[1:i].split(','):
                        word.append(letter)

                        backtracking(s[i + 1:], word)

                        word.pop()

                else:
                    word.append(s[0])

                    backtracking(s[1:], word)

                    word.pop()

        backtracking(s, [])
        ans.sort()
        return ans


if __name__ == '__main__':
    s = "{a,b}c{d,e}f"
    print(Solution().expand(s))
