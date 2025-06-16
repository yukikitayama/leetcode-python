"""
Backtracking(curr_sum, curr_comb, counter_hashmap)
  base case
    if curr sum is target
      save the curr combination
    if curr sum > target
      return

  transition
    iterate key-value pair
      k: candidate number
      v: count
    append candidate to curr combination
    decrement hashmap count
      if count is zero, delete the key
    recursion with curr comb, curr sum, hashmap
    backtrack
      pop the curr comb, get the key
      reduce curr sum
      increment hashmap

T:
  target: 30
  candidates: [1, 1, 1, 1,...]
    e.g. {1: 5, 2: 3}
  T: O(30)
"""

from typing import List
import collections


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(candidates)
        ans = set()

        def backtracking(curr_sum, curr_comb, curr_counter):

            # Base
            if curr_sum == target:
                print(curr_sum, curr_comb, curr_counter)
                ans.add(tuple(sorted(curr_comb)))
                return
            if curr_sum > target:
                return

            for k, v in curr_counter.items():

                curr_comb.append(k)
                next_counter = curr_counter.copy()
                next_counter[k] -= 1
                if next_counter[k] == 0:
                    del next_counter[k]

                backtracking(curr_sum + k, curr_comb, next_counter)

                # Backtracking
                popped_key = curr_comb.pop()

        backtracking(0, [], counter)

        # Set of tuples to list of list
        real_ans = []
        for el in ans:
            real_ans.append(list(el))

        return real_ans


