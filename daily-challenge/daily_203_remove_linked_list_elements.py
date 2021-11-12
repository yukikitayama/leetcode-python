from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head

        curr = head
        prev = sentinel

        # curr: ListNode(6), prev: ListNode(2)
        # curr: ListNode(6), prev: ListNode(5)
        while curr:

            # When curr.cal is the val, don't move prev pointer to the next
            # even if it typically does in the else block, because
            # delete the current node and curr pointer goes to the next, and
            # if prev pointer also goes to the next, curr and prev point at the same node
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next


head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val = 6
head = Solution().removeElements(head, val)
print()
while head:
    print(head.val)
    head = head.next
