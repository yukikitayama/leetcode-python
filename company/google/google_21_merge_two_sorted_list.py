from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Time complexity: O(n + m), where n and m are number of nodes in l1 and l2
# Because each iteration points at each node
# Space complexity: O(n + m), same n and m definition. In memory we save stack of merged linked list
# from n l1 and m l2

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
answer = Solution().mergeTwoLists(l1, l2)
while answer:
    print(answer.val)
    answer = answer.next
