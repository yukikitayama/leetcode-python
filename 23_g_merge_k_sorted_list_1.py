from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.nodes = []

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # head and point refer to the same object
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next

        for x in sorted(self.nodes):
            # Make a ListNode object and connect each ListNode
            point.next = ListNode(x)
            # Go to the next ListNode
            point = point.next

        # Return head of linked ListNodes
        # Remember head and point refer to the same object
        return head.next


"""
Time complexity
Let n be the total number of nodes
O(n) to collect all the values from ListNode and append them to list
O(nlogn) to sort the array by timsort
O(n) to create linked list
so O(n + nlogn + n) = O(2n + nlogn) = O(nlogn) 

Space complexity
O(n) to keep list of values of each node
"""


# head = point = ListNode(0)
# head = ListNode(0)
# point = ListNode(0)
head = ListNode(0)
point = head
print(head is point)
print(head == point)
print(head)
print(point)
