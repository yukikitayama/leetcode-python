"""
- Divisors are paired
  - if i is a divisor of n, n/i is also a divisor of n
- Make max heap
  - Because at last, we can return kth biggest factor if we access the head of max heap
  - After pushing a new number to max heap and if the size is more than k,
    we can pop the head which is k + 1th biggest factor which is not needed
- heappush() and heappop() time is O(logn) if there's n elements in the heap

Complexity
- Time is O(sqrt(n) * logk) because the outer for loop is range sqrt n
  and heap size is k and for each number in n, there's heappush and heappop
- Space is O(k) for heap
"""


import heapq


class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        def heappush_k(num):
            heapq.heappush(heap, -num)

            # Implementing max heap, pop the biggest number
            if len(heap) > k:
                heapq.heappop(heap)

        heap = []
        for x in range(1, int(n**0.5) + 1):
            if n % x == 0:
                heappush_k(x)

                # e.g. n: 15, x: 3, n % x: 15 % 3 = 0,
                # n // x: 15 // 3 = 5, 3 != 5: T,
                # e.g. n: 4, x: 2, n % x: 4 % 2 = 0, 2 is pushed to heap
                # n // x: 4 // 2 = 2, but we don't wanna push 2 again
                if x != n // x:
                    heappush_k(n // k)

        return -heapq.heappop(heap) if k == len(heap) else -1




n = 12
k = 3
n = 7
k = 2
n = 4
k = 4
n = 1
k = 1
n = 1000
k = 3
print(Solution().kthFactor(n, k))



