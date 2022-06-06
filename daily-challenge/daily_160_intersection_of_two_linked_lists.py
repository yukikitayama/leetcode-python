from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p_a = headA
        p_b = headB

        while p_a != p_b:
            # p_a.next will assign None to p_a at the end of linked list
            # so in the case two lists do not have intersection, both eventually
            # have None at the same time, and break this while loop
            p_a = headB if not p_a else p_a.next
            p_b = headA if not p_b else p_b.next

        return p_a


if __name__ == '__main__':
    headA = ListNode(2)
    headA.next = ListNode(6)
    headA.next.next = ListNode(4)
    headB = ListNode(1)
    headB.next = ListNode(5)

    headA = ListNode(1)
    shared = ListNode(2)
    headA.next = shared
    headB = ListNode(3)
    headB.next = shared

    ans = Solution().getIntersectionNode(headA, headB)
    print(ans.val)
