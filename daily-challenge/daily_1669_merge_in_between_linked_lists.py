# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = list1
        curr = prev.next
        counter = 1

        while counter < a:
            curr = curr.next
            prev = prev.next
            counter += 1
        # Here prev is node before a

        prev.next = list2

        # Get tail of list2
        while list2.next:
            list2 = list2.next

        # Get tail of remove part
        while counter < b:
            curr = curr.next
            counter += 1
        # Here curr is node at b

        list2.next = curr.next

        return list1
