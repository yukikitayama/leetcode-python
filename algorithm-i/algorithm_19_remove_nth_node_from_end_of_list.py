"""
- use left and right two pointers
- left and right pointers are apart by the given n
  - right pointer starts first,
  - when the distance between left and right pointers becomes n, left pointer starts
  - when right pointer reaches the end of the linked list,
    - we still have n distance between left and right
    - but left is nth from the end of the list
      - because right is at the end, and we know the distance between left and right is n
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # With dummy, we can remove either the node with 1 length linked list, ot
        # first node from more than 1 length linked list
        # With 1 length linked list, dummy.next will contain None
        # In removing the first node, remove the head, and dummy.next points at the second node
        dummy = ListNode(0)
        dummy.next = head
        right = dummy
        left = dummy

        # Right starts first and left stays until the distance between left and right becomes the given n
        # +1 because initially right is dummy head
        for _ in range(n + 1):
            right = right.next

        # Left starts
        # If length of linked list is 1, it will skip this while loop
        # This while loop also will be skipped when it removes the first node in the linked list
        while right is not None:
            right = right.next
            left = left.next

        # Remove nth node by skipping nth node
        # If length of linked is is 1, left.next.next is None,
        # and left.next (the only one node) will be None, so the return statement
        # returns None
        left.next = left.next.next

        return dummy.next


"""
If length of linked list is 2, and n is 2, it removes the first node
dummy - 1 - 2

After the for loop for right pointer
dummy - 1 - 2 - None
left            right
Skip while loop
left.next: 1 = left.next.next: 2
dummy - 2 - None
return dummy.next: 2
"""
head = [1,2,3,4,5]
n = 2
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
obj = Solution()
removed = obj.removeNthFromEnd(head, n)
print(removed.val)
while removed.next:
    removed = removed.next
    print(removed.val)

