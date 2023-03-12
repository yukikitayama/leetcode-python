from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = tail = ListNode()

        heap = []

        for i, l in enumerate(lists):
            if l:
                # (value of head of linked list, ListNode)
                # sorted by small value of heads
                heapq.heappush(heap, (l.val, i, l))

        # print(f'heap: {heap}')

        while heap:

            # get() removes and return an item from the queue
            val, i, node = heapq.heappop(heap)

            # print(f'  val: {val}, i: {i}, node: {node}')

            tail.next = ListNode(val)

            tail = tail.next
            node = node.next

            if node:
                # Reorder priority queue by small values
                heapq.heappush(heap, (node.val, i, node))

        return head.next


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]
    head = Solution().mergeKLists(lists)
    while head:
        print(head.val)
        head = head.next

