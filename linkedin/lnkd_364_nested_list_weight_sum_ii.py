"""
- DFS
  - find the max depth
  - Store each integer in hashmap
    - key: integer, value: depth
- Use the hashmap and max depth to calculate weighted sum
"""


from typing import List


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


class Solution:
    def __init__(self):
        self.ans = 0

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # Find max depth
        max_depth = self.depth(nestedList)

        # DFS and increment sum with weight
        self.weighted_sum(nestedList, 1, max_depth)

        return self.ans

    def depth(self, nestedList):
        curr_depth = 1

        for x in nestedList:

            if not x.isInteger():

                curr_depth = max(curr_depth, 1 + self.depth(x.getList()))

        return curr_depth

    def weighted_sum(self, nestedList, level, max_depth):
        for x in nestedList:
            if x.isInteger():
                self.ans += x.getInteger() * (max_depth - level + 1)

            else:
                self.weighted_sum(x.getList(), level + 1, max_depth)
