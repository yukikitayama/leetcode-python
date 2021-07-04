class Solution:
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1:
                    m1[w] = p
                if p not in m2:
                    m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False

            print(m1, m2)

            return True

        return filter(match, words)


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
sol = Solution()
answer = sol.findAndReplacePattern(words=words, pattern=pattern)
for a in answer:
    print(f'Answer: {a}')