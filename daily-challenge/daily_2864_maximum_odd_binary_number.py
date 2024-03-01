"""
Rightmost digit needs to be 1 to have odd number
if rightmost is 0
  move rightmost 1 to rightmost position
if rightmost is 1
  move leftmost 1 to

if single 1
  rightmost 1 is only answer
if multiple 1s
  move leftmost digit to left

eg
  "110"

  "101"
"""

import collections


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        arr = sorted(s)

        temp = arr[:-1]
        temp.reverse()
        arr[:-1] = temp[:]

        return "".join(arr)

    def maximumOddBinaryNumber1(self, s: str) -> str:
        counter = collections.Counter(s)

        return (counter["1"] - 1) * "1" + counter["0"] * "0" + "1"

