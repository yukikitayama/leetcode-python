from typing import List


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


"""
- Initialize depth to 1
- Initialize ans to 0
- Get length of the list
- Iterate each item in the list from 0 to the length
  - If the current item is integer
    - Increment ans by current integer * depth
  - If the current item is NestedInteger object,
    - Append 
"""


import collections


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth = 1
        ans = 0

        queue = collections.deque(nestedList)

        while queue:

            for _ in range(len(queue)):

                nested_integer = queue.popleft()

                if nested_integer.isInteger():
                    ans += nested_integer.getInteger() * depth

                else:
                    # This needs to be extend(), not append()
                    # because append will make [1, 2, 3, [4, 5, 6]],
                    # but we want [1, 2, 3, 4, 5, 6]
                    queue.extend(nested_integer.getList())

            depth += 1

        return ans
