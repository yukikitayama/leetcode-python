"""
"""


from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def is_subsequence(word):
            i = 0
            j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)

        ans = ''
        for word in dictionary:
            if is_subsequence(word):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word
        return ans


"""
Complexity
- Let n be the length of dictionary and m be the average length of words in dictionary
- Time is O(n*m) because for each word, check each character in the word
- Space is O(1)
"""


s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
# s = "abpcplea"
# dictionary = ["a","b","c"]
print(Solution().findLongestWord(s, dictionary))



