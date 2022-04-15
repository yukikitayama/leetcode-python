"""
- Heap?
"""


from typing import List
import collections
import heapq


class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            # Even if we are making min heap, word order is not min comparison
            # because at the end of solution, we reverse.
            # so count is descending, but we need the word to be ascending lexicographical order
            return self.word > other.word
        return self.count < other.count

    # This method is not necessary
    # def __eq__(self, other):
    #     return self.count == other.count and self.word == other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)

        # print(f'counter: {counter}')

        # Make min heap, but when the size of heap exceeds k, pop the minimum element
        # So the min heap keep the top k largest elements
        heap = []
        heapq.heapify(heap)
        for word, count in counter.items():

            heapq.heappush(heap, (Element(count, word), word))

            # Keep top k largest in min heap
            if len(heap) > k:
                heapq.heappop(heap)

            # print(f'  heap: {heap}')

        # But the answer format needs to be ordered by
        # descending counts, and ascending word lexico
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        # print(ans)

        return ans[::-1]


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    print(Solution().topKFrequent(words, k))
