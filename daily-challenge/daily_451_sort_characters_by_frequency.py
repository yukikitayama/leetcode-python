"""
- make Counter
- use built-in sort of list
  - sort(ascending=False, key=lambda x: count[x])
- return the join string
"""


import collections


class Solution:
    def frequencySort(self, s: str) -> str:

        # O(n)
        count = collections.Counter(s)
        # O(n)
        max_freq = max(count.values())

        # O(n)
        # Bucket sort
        # + 1 because need extra space character count 0, though it won't use it
        # bucket[number of characters][the characters list]
        buckets = [[] for _ in range(max_freq + 1)]
        for char, num in count.items():
            buckets[num].append(char)

        ans = []
        # Decreasing order
        # start: len(bucket) - 1 and end (exclusive): 0, because
        # i is the 0-based index, and it won't use index 0 (no character)
        # Still O(n) even though it's nested for loop, because
        # c * i is n
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                ans.append(c * i)

        return ''.join(ans)


"""
- Should implement the above box sort because the time is O(n)
- If you use built-in sort method, time is O(nlogn) which is not optimized
"""


s = "tree"
s = "cccaaa"
s = "Aabb"
print(Solution().frequencySort(s))



