"""
Problem
  intervals not necessarily sorted

Overlap
  when second start <= first end

Algo
  sort intervals by start ascending
  iterate intervals
    stack to collect interval
    if stack top interval end < curr interval start
      append to stack
    else
      stack pop
      merge
        case 1: [1, 3] and [2, 4]
          new interval [top start, curr end]
        case 2: [1, 4] and [2, 3]
          new interval [1, 4 (max of two intervals end)]
      stack append

Edge
  0 interval
    return empty array
  1 interval
    no merge, return array of array
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []

        for i in range(len(intervals)):

            interval = intervals[i]

            if not ans:
                ans.append(interval)

            else:
                if ans[-1][1] < interval[0]:
                    ans.append(interval)
                else:
                    popped = ans.pop()
                    end = max(popped[1], interval[1])
                    merged = [popped[0], end]
                    ans.append(merged)

        return ans
