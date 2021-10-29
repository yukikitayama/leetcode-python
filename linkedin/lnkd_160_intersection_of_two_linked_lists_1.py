"""
- compare id()?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        set_b = set()
        while headB:
            set_b.add(headB)
            headB = headB.next

        while headA:
            if headA in set_b:
                return headA
            headA = headA.next

        return None


"""
- Let m be the length of A linked list, n be the length of B linked list
- Time is O(m + n), space is O(n) for set
"""
