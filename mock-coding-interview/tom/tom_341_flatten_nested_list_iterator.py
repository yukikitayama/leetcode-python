# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       pass

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       pass

   def getList(self) -> ['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
       pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        nestedList.reverse()
        self.nested_list = list(nestedList)

    def next(self) -> int:
        self.preprocess()
        return self.nested_list.pop()

    def hasNext(self) -> bool:
        self.preprocess()
        return len(self.nested_list) > 0

    def preprocess(self) -> None:
        while self.nested_list and not self.nested_list[-1].isInteger():
            top = self.nested_list.pop()
            n_i = top.getList()
            n_i.reverse()
            self.nested_list.extend(n_i)


class NestedIterator1:
    def __init__(self, nestedList: [NestedInteger]):

        stack = []

        def recursion(nested_integer):

            while nested_integer:
                n_i = nested_integer.pop()

                if n_i.isInteger():
                    stack.append(n_i.getInteger())
                else:
                    recursion(n_i.getList())

        recursion(nestedList)

        # Stack got data from the right side, regardless integer or nested list, so need to reverse
        stack.reverse()
        self.array = stack[:]
        self.pointer = 0

    def next(self) -> int:
        num = self.array[self.pointer]
        self.pointer += 1
        return num

    def hasNext(self) -> bool:
        return self.pointer < len(self.array)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())