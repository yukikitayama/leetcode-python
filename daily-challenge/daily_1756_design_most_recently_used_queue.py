"""
linked list
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MRUQueue:

    def __init__(self, n: int):
        self.sentinel_head = ListNode(-1)
        # self.tail = self.sentinel_head
        curr = self.sentinel_head
        for i in range(n):
            node = ListNode(i + 1)
            curr.next = node
            curr = curr.next
        self.tail = curr

    def fetch(self, k: int) -> int:
        # Search kth node
        prev = self.sentinel_head
        for i in range(k - 1):
            prev = prev.next

        searched_node = prev.next

        # Add serached node to the next of tail
        self.tail.next = searched_node

        # Remove kth node
        prev.next = prev.next.next

        # Update tail
        self.tail = self.tail.next
        self.tail.next = None

        return searched_node.val


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)