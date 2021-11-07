"""
- One pass BFS
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


import collections


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        queue = collections.deque(nestedList)
        depth = 1
        max_depth = 0
        sum_of_elements = 0
        sum_of_products = 0
        while queue:
            max_depth = max(depth, max_depth)
            for _ in range(len(queue)):
                nested_integer = queue.popleft()
                if nested_integer.isInteger():
                    sum_of_elements += nested_integer.getInteger()
                    sum_of_products += nested_integer.getInteger() * depth
                else:
                    queue.extend(nested_integer.getList())
            depth += 1
        return (max_depth + 1) * sum_of_elements - sum_of_products
