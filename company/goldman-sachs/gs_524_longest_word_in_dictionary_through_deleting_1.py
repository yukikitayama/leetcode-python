"""
- Start: 2:17
- End: 2:32
- Solved: 1
- Saw solution: 0
- Optimized: 0

Idea
- Match a word in dictionary with a word made by deleting characters in s
  - Two pointers
- Sort dictionary
"""


s = "abpcplea"
# d = 'apple'
d = 'monkey'
# d = 'a'
p1 = 0
p2 = 0
while p1 < len(s) and p2 < len(d):
    if s[p1] == d[p2]:
        p1 += 1
        p2 += 1
    else:
        p1 += 1
print(f'p1: {p1}, p2: {p2}')
print(p2 == len(d))


from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def is_possible(word: str):
            p1 = 0
            p2 = 0
            while p1 < len(s) and p2 < len(word):
                if s[p1] == word[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p1 += 1
            return p2 == len(word)

        dictionary.sort()

        ans = ''
        for word in dictionary:
            if is_possible(word) and len(word) > len(ans):
                ans = word
        return ans


"""
Complexity
- Time
  - Let m be the length of s, and n be the average length of word in dictionary
    and k be the length of dictionary
  - Sort takes (nlogn), and the for loop takes O(k * max(m, n))
- Space is O(n) for sorting
"""


s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
s = "abpcplea"
dictionary = ["a","b","c"]
print(Solution().findLongestWord(s, dictionary))



