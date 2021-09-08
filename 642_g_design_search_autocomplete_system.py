from typing import List
from collections import defaultdict


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        # Dictionary Key: sentence, Value: time
        self.counts = defaultdict(int)
        for sentence, time in zip(sentences, times):
            self.counts[sentence] = time

        # All the matches by time decreasing order
        # Return only the first 3 items
        self.matches = []

        # Temporary storage to store currently input characters so far
        # It will be cleared with input #
        self.partial = []

    def input(self, c):
        # When input ends
        if c == '#':
            sentence = ''.join(self.partial)
            # Because we use defaultdict(int), even if a new sentence key does not exist in the dictionary,
            # the below does not throw an error, create a new key and be initialized with 1
            self.counts[sentence] += 1
            # Reset for the next input
            self.partial = []
            self.matches = []
            return []

        # When c is the first input before #
        # partial is length 0 list, so it's falseish, so the below is true
        if not self.partial:
            # 0 because this is only for the first input
            # -count because it will by hottest
            # e.g. a: 1, b: 2, c: 3 (numerically ascending but it's not hottest order)
            # => a: -1, b: -2, c: -3 (temporary)
            # sort() => c: -3, b: -2, a: -1 (numerically ascending, and if remove -, it's hottest order)
            self.matches = [(-count, sentence) for sentence, count in self.counts.items() if sentence[0] == c]
            self.matches.sort()
            # Drop count because we don't need it
            self.matches = [sentence for _, sentence in self.matches]
        # If in second input, partial contains one character, i: 1, which can point second element in array
        # because array starts with 0 index
        else:
            i = len(self.partial)
            self.matches = [sentence for sentence in self.matches if len(sentence) > i and sentence[i] == c]

        # Every time runs the below except #
        self.partial.append(c)

        return self.matches[:3]
