from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def get_first_half_tail(node):
            fast = node
            slow = node
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(node):
            """
            1 -> 2 -> 3 -> None
            None <- 1 <- 2 <- 3

            """
            prev = None
            curr = node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        first_tail = get_first_half_tail(head)
        second_head = reverse(first_tail.next)

        first_curr = head
        second_curr = second_head

        while second_curr:
            # print(second_curr.val, first_curr.val)

            if first_curr.val != second_curr.val:
                return False
            first_curr = first_curr.next
            second_curr = second_curr.next
        return True

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        curr = head
        prev = None
        n = 1
        while curr.next:
            n += 1
            curr.prev = prev
            prev = curr
            curr = curr.next
        # Here, the process at the last node not done yet
        curr.prev = prev

        # print(f"n: {n}")

        tail = curr
        curr = head

        # n: 5, n // 2 = 2, 3rd node no need to check
        while n // 2:
            n -= 1

            if curr.val != tail.val:
                return False

            curr = curr.next
            tail = tail.prev

        return True

    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True