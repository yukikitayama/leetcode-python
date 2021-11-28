from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # (ListNode value, index of lists)
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        # print(h)

        # Dummy head for iteration
        head = cur = ListNode(None)
        while h:
            # When heappopped, linked list at idx in lists is gone, so later needs to heapq.heappush to fill the empty
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            # 2 equals because we want both node and lists[idx] refer to the same object
            # To add back in the ListNode, we need to retrieve ListNode from lists
            # Update the head of linked list at idx in lists
            # and get ListNode
            node = lists[idx] = lists[idx].next

            # Above, when .next is None, node is None, so below if is ignored
            # heappop made item in lists at idx empty, so the below push again
            if node:
                heapq.heappush(h, (node.val, idx))

        # head is dummy so return .next
        return head.next


"""
Implementation
heappush can push a tuple. In that case, first element is the priority.

Time complexity
Let k be the length of lists, and n be the total number of nodes.
Priority queue always contains at most the length of lists
So priority pop and insert takes O(logk), and we have while loop taking O(n)
so O(nlogk)

Space complexity
O(k) for priority queue. O(n) for the new linked list
"""


lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
print(Solution().mergeKLists(lists))
