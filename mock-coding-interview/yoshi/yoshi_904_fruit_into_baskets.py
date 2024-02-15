"""
Hashmap
  T: O(N)
Greedy
  Sort hashmap, T: (logN)

Heap
  (type_of_fruit, count_of_fruit)

---
Two pointers
  left
  right
  To know if I have twp types of fruit, I use hashset
"""

from typing import List
import collections


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # counter = collections.Counter(fruits)
        # # [2, 1, 0] for eg2
        # sorted_type = sorted(counter.keys(), key=lambda k: counter[k], reverse=True)

        # ans = 0
        # k = 2
        # i = 0

        # while len(counter) > 0 and k > 0:
        #     fruit = sorted_type[i]
        #     ans += counter[fruit]
        #     k -= 1
        #     i += 1
        #     del counter[fruit]

        # return ans

        counter = collections.defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(fruits)):

            fruit = fruits[right]

            counter[fruit] += 1

            while len(counter.keys()) == 3:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans

