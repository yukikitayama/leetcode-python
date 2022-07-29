"""
- counter
"""


from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def match(word):

            w_to_p = {}
            p_to_w = {}

            for w, p in zip(word, pattern):

                if w not in w_to_p:
                    w_to_p[w] = p
                if p not in p_to_w:
                    p_to_w[p] = w

                if (w_to_p[w], p_to_w[p]) != (p, w):
                    return False

            return True

        ans = [word for word in words if match(word)]
        return ans


if __name__ == '__main__':
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"
    print(Solution().findAndReplacePattern(words, pattern))
