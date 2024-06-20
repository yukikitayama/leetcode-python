# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """S: O(logN)"""

        def helper(start, end):

            # Terminate
            if start is None or start == end:
                return

            # Terminate: only one node
            if start.getNext() == end:
                start.printValue()
                return

            # Find middle node by two pointers
            fast = start
            slow = start
            while fast != end and fast.getNext() != end:
                fast = fast.getNext().getNext()
                slow = slow.getNext()

            # Here slow is middle
            # To print rightmost nodes first, recursion to the right part first
            helper(slow, end)
            helper(start, slow)

        helper(head, None)

    def printLinkedListInReverse2(self, head: 'ImmutableListNode') -> None:
        """Constant space"""
        curr_end = None

        # Eventually at the bottom, head will be curr_end by curr_end = curr_node
        while head != curr_end:

            # Every time iteration restarts from the beginning
            curr_node = head

            while curr_node.getNext() != curr_end:
                curr_node = curr_node.getNext()

            # Here current node is the current end node
            curr_node.printValue()

            # Update current end with current node
            curr_end = curr_node

    def printLinkedListInReverse1(self, head: 'ImmutableListNode') -> None:
        """Naive approach, T: O(N), S: O(N)"""
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.getNext()
        for i in range(len(nodes) - 1, -1, -1):
            nodes[i].printValue()