"""
Is logs sorted?

length
  end num - start num + 1

initialize ans length of n with 0s

Sort by the first, and last number in ascending

Stack
  if start
    append to stack
  if end
    pot top stack
    compute length and increment ans array

Algo
  Iterate from left to right?
  diff start and end: end - start + 1
  diff start-start/end-end: end - start
"""

from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        ans = [0] * n

        stack = []

        prev = 0

        for i in range(len(logs)):

            log = logs[i].split(":")

            id_ = int(log[0])
            status = log[1]
            time = int(log[2])

            if status == "start":

                if stack:
                    top_id = stack[-1]
                    ans[top_id] += time - prev

                stack.append(id_)
                prev = time

            elif status == "end":
                top_id = stack.pop()
                ans[top_id] += time - prev + 1
                # +1 because try not to count end -> start sequence, but end -> end count by above
                prev = time + 1

        return ans
