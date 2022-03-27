from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        used = [False] * len(s)

        # print(f'used: {used}')

        for word in words:
            start = s.find(word)
            last = len(word)

            # If find() doesn't find, return -1
            while start != -1:
                for i in range(start, start + last):
                    used[i] = True

                # 2nd arg is start position inclusive
                start = s.find(word, start + 1)

        # print(f'used: {used}')

        # Use a list of string to avoid blow up making strings
        ans = []
        i = 0
        while i < len(s):
            if used[i]:
                ans.append('<b>')
                # Keep adding character after <b> as long as bold indicated by used boolean array
                while i < len(s) and used[i]:
                    ans.append(s[i])
                    i += 1
                ans.append('</b>')

            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)


if __name__ == '__main__':
    s = "abcxyz123"
    words = ["abc", "123"]
    s = "aaabbcc"
    words = ["aaa", "aab", "bc"]
    print(Solution().addBoldTag(s, words))
