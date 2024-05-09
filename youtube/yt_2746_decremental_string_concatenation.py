"""
dp(index to words array, first character, rear character)

  # Base case
  if index == 0:
    return len(first word)
"""

from typing import List
import functools


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:

        # edge case
        if len(words) == 1:
            return len(words[0])

        @functools.cache
        def dp(curr_i, prev_front, prev_back):

            # Base case
            if curr_i == len(words):
                return 0

            # State transition
            # Given current word is A and prev word is B, we have 2 choices to concat; AB or BA
            return len(words[curr_i]) + min(

                # Form AB
                # If curr word (A) back is equal to prev word (B) front, delete one character
                # For next word, AB front is curr's (A) front, and AB back is prev's (B) back
                -(1 if words[curr_i][-1] == prev_front else 0) + dp(curr_i + 1, words[curr_i][0], prev_back),

                # Form BA
                # If curr word (A) front is equal to prev word (B) back, delete one character
                # For next word, BA front is prev's (B) front, and BA back is curr's (A) back
                -(1 if prev_back == words[curr_i][0] else 0) + dp(curr_i + 1, prev_front, words[curr_i][-1])
            )

        return len(words[0]) + dp(1, words[0][0], words[0][-1])