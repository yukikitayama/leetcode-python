"""
total wait initializes with 0
initialize prev finish with first customer arrival
iterate customers
  current finish = prev finish + prepare time
  each wait = current finish - each arrival
  increment total wait with each wait
return total wait divided by customers array length
"""

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait = 0
        prev_finish = customers[0][0]

        for arrival_time, prepare_time in customers:

            curr_finish = max(prev_finish, arrival_time) + prepare_time
            wait = curr_finish - arrival_time
            total_wait += wait

            # print(f"prev_finish: {prev_finish}, curr_finish: {curr_finish}, arrival_time: {arrival_time}, wait: {wait}")

            prev_finish = curr_finish

        return total_wait / len(customers)