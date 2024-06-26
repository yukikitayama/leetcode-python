# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        ans = 0
        queue = collections.deque(nestedList)
        depth = 1

        while queue:

            for _ in range(len(queue)):

                ni = queue.popleft()

                if ni.isInteger():
                    ans += depth * ni.getInteger()
                else:
                    queue.extend(ni.getList())

            depth += 1

        return ans

    def depthSum1(self, nestedList: List[NestedInteger]) -> int:
        ans = 0
        depth = 1

        while True:

            next_ = []

            for _ in range(len(nestedList)):

                ni = nestedList.pop()

                if ni.isInteger():
                    num = ni.getInteger()
                    ans += num * depth

                else:
                    next_ni = ni.getList()
                    next_.extend(next_ni)

            depth += 1
            nestedList = next_

            if not nestedList:
                break

        return ans
