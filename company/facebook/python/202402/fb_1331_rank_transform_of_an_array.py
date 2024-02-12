"""
min heap
  push every element
    (num in arr, index in arr)

when pop
  prev num and rank
    prev starts with -inf
    rank starts with 0
    when pop and popped num is bigger than prev
      count up rank
    insert ans
    update prev
"""


class Solution:
    # def arrayRankTransform(self, arr: List[int]) -> List[int]:
    #     min_heap = []
    #     heapq.heapify(min_heap)

    #     for i in range(len(arr)):
    #         num = arr[i]
    #         heapq.heappush(min_heap, (num, i))

    #     ans = [None] * len(arr)
    #     prev = float("-inf")
    #     rank = 0

    #     while min_heap:
    #         curr_num, curr_index = heapq.heappop(min_heap)
    #         if curr_num > prev:
    #             rank += 1
    #         ans[curr_index] = rank

    #         prev = curr_num

    #     return ans

    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        # Create rankings
        sorted_arr = sorted(arr)
        rank = collections.defaultdict(int)
        for i in range(len(arr)):
            num = sorted_arr[i]
            if num not in rank:
                rank[num] = len(rank) + 1

        # Convert given array to ranking array
        ans = []
        for i in range(len(arr)):
            num = arr[i]
            ans.append(rank[num])
        return ans
