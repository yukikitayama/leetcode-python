"""
Hashmap
  k, char
  v, order integer

Sort s by the order priority
  If char in s doesn't appear in hashmap, assign order float("inf")
Use min heap
Iterate s
  Add (order, char) to min heap

Pop from heap and construct output string

Edge
  a char in s doesn't appear in order

T: O(nlogn)
S: O(n)
"""

import collections


class Solution:
    # Min heap
    # def customSortString(self, order: str, s: str) -> str:
    #     char_to_order = collections.defaultdict(int)

    #     for i in range(len(order)):
    #         char_to_order[order[i]] = i

    #     min_heap = []
    #     heapq.heapify(min_heap)

    #     for i in range(len(s)):

    #         curr_char = s[i]

    #         # Get priority
    #         if curr_char in char_to_order:
    #             curr_order = char_to_order[curr_char]
    #         else:
    #             curr_order = float("inf")

    #         heapq.heappush(min_heap, (curr_order, curr_char))

    #     ans = []
    #     while min_heap:
    #         curr_order, curr_char = heapq.heappop(min_heap)
    #         ans.append(curr_char)
    #     return "".join(ans)

    # Counter
    def customSortString(self, order: str, s: str) -> str:
        counter = collections.Counter(s)

        ans = []

        for order_char in order:
            if order_char in counter:
                ans.append(order_char * counter[order_char])

        order_set = set(order)
        for counter_char in counter:
            if counter_char not in order_set:
                ans.append(counter_char * counter[counter_char])

        return "".join(ans)