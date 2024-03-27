# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:

        # Find middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Merge first and second parts
        first = head
        second = prev
        while second.next:
            next_ = first.next
            first.next = second
            first = next_

            next_ = second.next
            second.next = first
            second = next_

    def reorderList1(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        index_to_node = {}
        index = 0
        curr = head
        while curr:
            index_to_node[index] = curr
            index += 1
            curr = curr.next

        n = len(index_to_node)

        # Edge
        if n == 1:
            return head

        for i in range(n // 2):
            curr = index_to_node[i]

            if i != 0:
                prev.next = curr

            prev = curr

            curr = index_to_node[n - i - 1]
            prev.next = curr
            prev = curr

        # Odd
        if n % 2 != 0:
            curr = index_to_node[n // 2]
            prev.next = curr
            curr.next = None
        # Even
        else:
            prev.next = None