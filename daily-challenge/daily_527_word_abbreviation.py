from typing import List


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:

        def abbrev(word, i=0):
            # If the abbreviation does not make the word shorter, then keep it as the original.
            if len(word) - i <= 3:
                return word

            return word[:i + 1] + str(len(word) - i - 2) + word[-1]

        n = len(words)

        ans = list(map(abbrev, words))

        prefix = [0] * n

        for i in range(n):
            while True:
                dupes = set()
                for j in range(i + 1, n):
                    if ans[i] == ans[j]:
                        dupes.add(j)

                if not dupes:
                    break

                dupes.add(i)

                for k in dupes:

                    prefix[k] += 1
                    ans[k] = abbrev(words[k], prefix[k])

        return ans


if __name__ == '__main__':
    words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
    # ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
    print(Solution().wordsAbbreviation(words))
