from typing import List
import collections
import heapq


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, Pair(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = [p.word for p in sorted(heap, reverse=True)]
        return ans


class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        ans = heapq.nsmallest(k, counter.keys(), key=lambda x: (-counter[x], x))
        return ans