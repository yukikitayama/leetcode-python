"""
- Initialize ans to 0
- Sort event by starting time
- Current value
- backtracking
  - pick one event
  - increment the current value
  - pick next event if
    - next event startTime > current event endTime
  - Backtracking by
    - decrement the current value by the previous value
    - pick another next event
"""


from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        events.sort(key=lambda x: x[0])

        # print(f'events: {events}')

        def backtracking(prev_end_time, total_value, start_index, count):

            # print(f'total_value: {total_value}, start: {start_index}')

            nonlocal ans

            if count == 2:
                ans = max(ans, total_value)
                return

            if start_index == len(events):
                ans = max(ans, total_value)
                return

            for i in range(start_index, len(events)):
                start_time, end_time, value = events[i]

                if prev_end_time < start_time:
                    total_value += value
                    backtracking(end_time, total_value, i + 1, count + 1)

                    total_value -= value

                if count < 2:
                    ans = max(ans, total_value)

        ans = 0

        for i, event in enumerate(events):

            start_time, end_time, value = event

            backtracking(end_time, value, i + 1, 1)
            # print()

        return ans


events = [[1,3,2],[4,5,2],[2,4,3]]  # 4
events = [[1,3,2],[4,5,2],[1,5,5]]  # 5
events = [[1,5,3],[1,5,1],[6,6,5]]  # 8
# events = [[10,83,53],[63,87,45],[97,100,32],[51,61,16]]  # 85
print(Solution().maxTwoEvents(events))





