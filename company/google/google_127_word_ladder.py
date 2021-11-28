from collections import defaultdict, deque
from typing import List
import pprint


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Edge case
        if endWord not in wordList:
            return 0

        length = len(beginWord)

        # Intermediate form to list of words
        intermediate_to_list_of_words = defaultdict(list)
        for word in wordList:
            for i in range(length):
                intermediate_to_list_of_words[word[:i] + '*' + word[i + 1:]].append(word)
        print('Intermediate word to list of words dictionary')
        # pprint.pprint(intermediate_to_list_of_words)

        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}

        # O(N)
        while queue:
            current_word, level = queue.popleft()

            # O(M)
            for i in range(length):

                intermediate_word = current_word[:i] + '*' + current_word[i + 1:]

                # O(M)
                for word in intermediate_to_list_of_words[intermediate_word]:

                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))

                # Avoid visiting again
                intermediate_to_list_of_words[intermediate_word] = []

        return 0


"""
Time complexity

"""


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))
