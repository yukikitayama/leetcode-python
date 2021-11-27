"""
- Iterate both linked list to the end
  - Make prev pointer in iteration
- Iterate from end to start
  - make carry
  - Append sum to stack
- Make linked list from the stack
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_list(head):
            last = None
            while head:
                # Keep the following nodes
                tmp = head.next
                # Connect previous node to current node next to reverse
                head.next = last
                # Keep previous node for the next iteration
                last = head
                # next node going to be the new head
                head = tmp
            return last

        l1 = reverse_list(l1)
        l2 = reverse_list(l2)

        head = None
        carry = 0
        while l1 or l2:
            # Get current value. 0 is when the other linked list already has no more nodes
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0

            # current value from 0 to 9
            val = (carry + x1 + x2) % 10

            # Value to carry to the next big digit
            carry = (carry + x1 + x2) // 10

            # Make current node
            curr = ListNode(val)

            # Connect the nodes already made to the next of the current node
            # so the nodes made earlier go to the end of the linked list
            curr.next = head
            head = curr

            # Move pointer
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head


"""
reverse_list
5 -> 6 -> 4
last: None, head: TreeNode(5), while: T
  tmp: TreeNode(6).next: TreeNode(4), head.next: TreeNode(5).next = None, last: TreeNode(5),
  head: TreeNode(6).next: TreeNode(4), while: T,
    tmp = TreeNode(4), head.next: TreeNode(6).next = last = TreeNode(5), last: TreeNode(6),
    head: TreeNode(4), while: T,
      tmp: TreeNode(4).next = None, head.next: TreeNode(4).next = TreeNode(6), last: TreeNode(4),
      head: None. while: F
return last: TreeNode(4)
"""


l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))
ans = Solution().addTwoNumbers(l1, l2)
while ans:
    print(ans.val)
    ans = ans.next




