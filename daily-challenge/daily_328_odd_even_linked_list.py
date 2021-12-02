"""
- Start: 6:55
- End: 7:04
- Saw solution: 1

"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head
        even = head.next
        even_head = even

        # Only check even elements because even always after odd nodes in while loop
        while even and even.next:

            # e.g. 1 -> 2 -> 3 -> 4 -> 5
            # odd: 1, even: 2
            # odd.next: 3, odd: 3
            # even.next: 4, even: 4

            # Update next
            odd.next = even.next
            # Update curr
            odd = odd.next

            # Update next
            even.next = odd.next
            # Update curr
            even = even.next

        # Hear odd is tail of odd linked list
        odd.next = even_head
        # head remains as the head of odd linked list
        return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# [1,3,5,2,4]
ans = Solution().oddEvenList(head)

while ans:
    print(ans.val)
    ans = ans.next


