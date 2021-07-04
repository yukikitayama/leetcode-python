class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None

        # m: left, n: right
        m = head,
        n = head
        stop = False

        def recurseAndReverse(n, left, right):
            nonlocal m, stop

            if right == 1:
                return

            n = n.next

            if left > 1:
                m = m.next

            recurseAndReverse(n, left - 1, right - 1)

            if m == n or n.next == m:
                stop = True

            if not stop:
                n.val, m.val = m.val, n.val

                n = n.next

        recurseAndReverse(m, left, right)

        return head