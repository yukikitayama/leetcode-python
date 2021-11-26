"""
Result
- Start: 12:22
- End: 12:40
- Solved: 1
- Saw solution: 0
- Optimized: 0

Idea
- Sort by descending
- Make a set from words list
- Iterate a word
  - remove a last character at a time
  - check whether the reduced word in the set

- Brute force
"""


from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(reverse=True, key=lambda x: len(x))

        # print(f'sorted words: {words}')

        set_words = set(words)

        ans = ''

        for word in words:

            if ans != '' and len(word) < len(ans):
                break

            # print(f'  word: {word}')

            tmp = word

            while len(word):

                # print(f'    word: {word}')

                if word in set_words:
                    word = word[:-1]
                else:
                    break

            if ans == '' and len(word) == 0:
                ans = tmp
            elif len(tmp) == len(ans) and tmp < ans and len(word) == 0:
                ans = tmp

        return ans


"""
Complexity
- Let n be the length of words, m be the max length of word in words 
- Time
  - Sorting words is O(nlogn)
  - Find the answer word is O(n*m)
- Space is O(n) for sorting and O(m) for the temporary word
"""


words = ["w","wo","wor","worl","world"]  # world
# words = ["a","banana","app","appl","ap","apply","apple"]  # apple
words = ["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]
# breakfast
print(Solution().longestWord(words))


