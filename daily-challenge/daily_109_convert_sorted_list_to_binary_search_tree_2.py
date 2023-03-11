from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_middle(self, head):
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # When slow == head
        if prev:
            prev.next = None

        return slow

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None

        mid_list_node = self.find_middle(head)

        tree_node = TreeNode(mid_list_node.val)

        # Base case when a node becomes only one element in linked list
        if head == mid_list_node:
            return tree_node

        tree_node.left = self.sortedListToBST(head)
        tree_node.right = self.sortedListToBST(mid_list_node.next)

        return tree_node



