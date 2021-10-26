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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):
            curr_sum = 0
            for nested_item in nested_list:

                if nested_item.isInteger():
                    curr_sum += nested_item.getInteger() * depth

                else:
                    curr_sum += dfs(nested_item.getList, depth + 1)

            return curr_sum

        return dfs(nestedList, 1)


"""
- Let d be the maximum depth in the list, and n be the nested items in the list
- Time is O(n) because it needs to visited all the items in recursion and for loop
- Space is O(d) because it has the recursion stack stacked up to maximum depth
"""