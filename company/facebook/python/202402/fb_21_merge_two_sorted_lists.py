from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sentinel_head = ListNode()
        curr = sentinel_head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return sentinel_head.next

    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sentinel_head = ListNode()
        curr = sentinel_head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next

            curr = curr.next

        if list1:
            while list1:
                curr.next = ListNode(list1.val)
                list1 = list1.next
                curr = curr.next

        elif list2:
            while list2:
                curr.next = ListNode(list2.val)
                list2 = list2.next
                curr = curr.next

        return sentinel_head.next
