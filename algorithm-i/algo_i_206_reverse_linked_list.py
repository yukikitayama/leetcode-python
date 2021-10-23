"""
- curr_node = head,
  - curr_node: ListNode(1)
- prev_node = curr_node.next
  - prev_node: ListNode(2)
- curr_node needs to be ListNode(2), and prev_node needs to be ListNode(3)
  - curr_node = prev_node
  - prev_node = curr_node.next

- ListNode(2) = ListNode(1).next
- ListNode(3) = ListNode(2).next
- ListNode(2).next = ListNode(1)
- ListNode(3).next = ListNode(2)
- ...
- ListNode(5).next = ListNode(4)
- return ListNode(5)
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr_node = head
        prev_node = None

        while curr_node:

            next_temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_temp

        return prev_node


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ans = Solution().reverseList(head)
while ans:
    print(ans.val)
    ans = ans.next