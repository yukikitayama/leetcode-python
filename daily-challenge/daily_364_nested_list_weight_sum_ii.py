# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
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


from typing import List
import collections


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = 0
        depth = 1
        sum_of_array = 0
        weighted_sum_of_array = 0
        queue = collections.deque(nestedList)

        while queue:

            max_depth = max(max_depth, depth)

            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr.isInteger():
                    sum_of_array += curr.getInteger()
                    weighted_sum_of_array += depth * curr.getInteger()
                else:
                    queue.extend(curr.getList())

            depth += 1

        return (max_depth + 1) * sum_of_array - weighted_sum_of_array


nestedList = [[1, 1], 2, [1, 1]]
# 8

