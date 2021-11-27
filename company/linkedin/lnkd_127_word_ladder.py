"""
- Initialize ans to 0
- Backtracking
  - If a current word is in wordList
    - Backtracking with counter incremented, and index
    - Replace current char with other 26 lower english letters
"""


from typing import List
import collections
import pprint


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (
                endWord not in wordList
                or not endWord
                or not beginWord
                or not wordList
        ):
            return 0

        L = len(beginWord)

        # Hashmap with key the generic word and value a list of words having the same intermediate
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

        pprint.pprint(all_combo_dict)

        # Starts from 1 because the example counts the initial states
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}

        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]

                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        # Plus one because for each word, one transformation happened
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))

                # ?
                # all_combo_dict[intermediate_word] = []

        return 0


"""
Complexity
- Let m be the length of each word, and n be the total number of words in wordList
- Time is O(m^2*n) because making hashmap costs this time, for each word n times and for each m range,
  substring to make a generic word by m times. And in BFS go to N words, each word try m intermediate combinations,
  and m substring operations.
- Space is O(m^2 * n) for the hashmap 
"""


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# beginWord = 'aaa'
# endWord = 'aab'
# wordList = ['aab', 'aac']
print(Solution().ladderLength(beginWord, endWord, wordList))
