from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    When current reached k, initialize end to head, and start traversing together with curr
    So end is k behind curr. When curr reaches the end of linked list, end is kth node from the end of the list
    """
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        end = None
        while curr:
            n += 1

            if end:
                end = end.next

            if n == k:
                front = curr
                end = head
            curr = curr.next

        # print(f'n: {n}, front.val: {front.val}, end.val: {end.val}')

        front.val, end.val = end.val, front.val

        return head


class Solution2:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0

        curr = head
        while curr:
            n += 1
            if n == k:
                front = curr

            curr = curr.next

        # print(f'n: {n}, front.val: {front.val}')

        end = head
        for _ in range(1, n - k + 1):
            end = end.next

        front.val, end.val = end.val, front.val

        return head


class Solution1:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0

        curr = head
        while curr:
            n += 1
            curr = curr.next

        # print(f'n: {n}')

        front = head
        for _ in range(1, k):
            front = front.next

        # print(f'front.val: {front.val}')

        end = head
        for _ in range(1, n - k + 1):
            end = end.next

        # print(f'end.val: {end.val}')

        front.val, end.val = end.val, front.val

        return head


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    ans = Solution().swapNodes(head, k)
    while ans:
        print(ans.val)
        ans = ans.next
