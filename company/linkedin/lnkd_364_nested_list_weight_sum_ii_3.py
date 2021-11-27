"""
- One pass recursion
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


"""
- First get max depth
- Then DFS or BFS
"""


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):

            sum_of_products = 0
            sum_of_elements = 0
            max_depth = 0

            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    sum_of_products += nested_integer.getInteger() * depth
                    sum_of_elements += nested_integer.getInteger()
                    max_depth = max(max_depth, depth)
                else:
                    result = dfs(nested_integer.getList(), depth + 1)
                    sum_of_products += result[0]
                    sum_of_elements += result[1]
                    max_depth = max(max_depth, result[2])
            return sum_of_products, sum_of_elements, max_depth

        result = dfs(nestedList, 1)
        sum_of_products = result[0]
        sum_of_elements = result[1]
        max_depth = result[2]
        return (max_depth + 1) * sum_of_elements - sum_of_products









