from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:
            return head

        def recurse_and_reverse(right_node, left, right):

            # Becuase we don't have prev pointer in list node, we keep right_node in a function,
            # so in memory, previous right_node is available
            nonlocal left_node, stop

            # print(f'left: {left}, left_node.val: {left_node.val}, right: {right}, right_node.val: {right_node.val}')

            # Terminate if right pointer reached the end of the reverse list
            if right == 1:
                return

            # Iterate
            right_node = right_node.next

            # Keep finding the start node of the reverse list
            # and stop, but right node could keep iterating
            if left > 1:
                left_node = left_node.next

            # Keep recursing
            recurse_and_reverse(right_node, left - 1, right - 1)

            # 1st condition for odd, and 2nd condition for even length reverse list
            if left_node == right_node or right_node.next == left_node:
                stop = True

            if not stop:

                # print(f'  reversing, left_node.val: {left_node.val}, right_node.val: {right_node.val}')

                left_node.val, right_node.val = right_node.val, left_node.val
                left_node = left_node.next

                # print(f'  reversed, left_node.val: {left_node.val}, left_node: {left_node}, right_node.val: {right_node.val}, right_node: {right_node}')

        left_node = head
        right_node = head
        stop = False

        recurse_and_reverse(right_node, left, right)

        return head


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left = 2
    right = 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    left = 2
    right = 5
    print(Solution().reverseBetween(head, left, right))
