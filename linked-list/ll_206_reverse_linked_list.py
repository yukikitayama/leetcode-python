from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize prev to None because there's nothing before head
        prev = None
        curr = head

        # 1 -> 2 -> 3 -> 4 -> 5
        # prev: None, curr: 1, temp: curr.next = 1.next = 2,
        # prev: 4, curr: 5, temp: None, curr.next: 4, prev: 5, curr: None

        # curr will eventually be None because curr will be temp, and temp will be curr.next, and it will be None
        while curr:

            temp = curr.next
            # This actually reverses the order
            # prev -> curr => curr -> prev
            curr.next = prev
            prev = curr
            curr = temp

        return prev
