"""
eg1
Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]
Person 0
  6, 8, 11,
Person 1 can see person 2 but not person 4
  p1: 6, p4: 11, max(p2, p3) = 8,

eg2
heights = [5,1,2,3,10]
Output: [4,1,1,1,0]

Naive
  two pointers
    left end, right end
    scan between two ends
  T: O(N^3)

Simply formula with two pointers
[10,6,8,5,11,9]
  10,
    max_so_far starts with 0
    apply formula
      if formula succeeds, increment
    updated max_so_far
  T: O(N^2)

[5, 11, 9]
  stack: [11]
[8,5,11,9]
  stach: [11, 5]
[6,8,5,11,9]
  stack: [11, 8]
[10, 6,8,5,11,9]
  stack: [11, 8, 6]

Better approach
  Stack
    decresing order
    min val, max so far
  Scan from right
    starts with empty stack
    right val starts with 0
    length of empty stack is the number of people to see.

    if current number is smaller than the top of stack,
      append
    if current number is bigger than the top of stack
      keep popping

    length of stack is the number of people to see

    https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/
"""

from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        stack = []
        ans = [0] * len(heights)

        for i in range(len(heights) - 1, -1, -1):

            # print(f"i: {i}, current height: {heights[i]}, stack: {stack}")

            #
            # ans.append(len(stack))
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            if stack:
                count += 1

            stack.append(heights[i])
            ans[i] = count
            # [5, 1, 2, 3, 10], when 2, stack: [10, 3],

        # ans.reverse()

        return ans

    def canSeePersonsCount1(self, heights: List[int]) -> List[int]:
        ans = []

        for left in range(len(heights) - 1):
            right = left + 1
            counter = 0
            max_so_far = 0
            while right < len(heights):
                min_val = min(heights[left], heights[right])
                if min_val > max_so_far:
                    counter += 1
                max_so_far = max(max_so_far, heights[right])
                right += 1

            ans.append(counter)

        ans.append(0)

        return ans