from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            ans = Node(insertVal)
            ans.next = ans
            return ans

        prev = head
        curr = head.next
        insert = False

        # Only loop once
        while True:

            # Middle
            if prev.val <= insertVal <= curr.val:
                insert = True

            # Tail (In middle prev < curr)
            # Here prev is tail and curr is head
            if curr.val < prev.val:
                # InsertVal is bigger than tail or insertVal is smaller than head
                if prev.val <= insertVal or insertVal <= curr.val:
                    insert = True

            if insert:
                insert_node = Node(insertVal)
                prev.next = insert_node
                insert_node.next = curr
                return head

            prev, curr = curr, curr.next

            # Finish one iteration
            if prev == head:
                break

        # All values in linked list are the same
        insert_node = Node(insertVal)
        prev.next = insert_node
        insert_node.next = curr
        return head


if __name__ == "__main__":
    head = Node(3)
    head.next = Node(4)
    head.next.next = Node(1)
    head.next.next.next = head
    insertVal = 2
    ans = Solution().insert(head, insertVal)

    while ans:
        print(ans.val)
        ans = ans.next
