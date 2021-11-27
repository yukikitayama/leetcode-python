from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()

        curr_node = ans

        while l1 and l2:

            if l1.val <= l2.val:
                curr_node.next = l1
                l1 = l1.next

            else:
                curr_node.next = l2
                l2 = l2.next

            curr_node = curr_node.next

            # print(curr_node.val)

        # Because either l1 or l2 is None, and the other is still have a node or nodes,
        # Each linked list is sorted, so we can just directly connect the rest of the linked list
        curr_node.next = l1 if l1 is not None else l2

        # print(curr_node.val)

        return ans.next


"""
- Let m and n be the length of l1 and l2. 
- Time is O(m + n) for while loop increments either l1 or l2 in each iteration
- Space is O(1)
"""


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
ans = Solution().mergeTwoLists(l1, l2)
