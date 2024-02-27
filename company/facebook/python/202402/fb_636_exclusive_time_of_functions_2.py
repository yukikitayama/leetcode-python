"""
Hashmap
  k: function id
  v: total execution time
Stack
  [(function id, start time), (), ...]
Iteration
  if start
    if empty stack
      append start
    if stack contains another start
      Compute stack top function execution time
        update hashmap

  if end,
    pop stack top
    compute execution time
    update hashmap
    update stack top start time with end time
"""

from typing import List
import collections


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev = 0

        for i in range(len(logs)):

            id_, type_, time_ = logs[i].split(":")
            id_ = int(id_)
            time_ = int(time_)

            if type_ == "start":

                if not stack:
                    stack.append(id_)

                else:
                    prev_id = stack[-1]
                    ans[prev_id] += time_ - prev
                    stack.append(id_)

                prev = time_

            elif type_ == "end":
                prev_id = stack.pop()
                ans[prev_id] += time_ - prev + 1
                prev = time_ + 1

        return ans

    def exclusiveTime1(self, n: int, logs: List[str]) -> List[int]:

        id_to_time = collections.defaultdict(int)
        stack = []

        for i in range(len(logs)):

            id_, type_, time_ = logs[i].split(":")
            time_ = int(time_)

            if type_ == "start":
                if not stack:
                    stack.append([id_, time_])

                else:
                    prev_id, prev_start = stack[-1]
                    duration = time_ - prev_start
                    id_to_time[prev_id] += duration

                    stack.append([id_, time_])

            elif type_ == "end":
                prev_id, prev_start = stack.pop()
                duration = time_ - prev_start + 1
                id_to_time[prev_id] += duration

                # Update stack top start time
                if stack:
                    stack[-1][1] = time_ + 1

            # print(f"stack: {stack}, hashmap: {id_to_time}")

        # print(id_to_time)
        # print(stack)

        ans = [0] * len(id_to_time)
        for id_, v in id_to_time.items():
            ans[int(id_)] = v
        return ans
