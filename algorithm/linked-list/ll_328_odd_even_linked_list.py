"""
- 4 pointers
  - head: head of the entire linked list and also a head of odd linked list
  - odd: current node in odd linked list, eventually tail of odd linked list
  - even_head: head of the even linked list
  - even: current node if even linked list, eventually tail of even linked list
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head




