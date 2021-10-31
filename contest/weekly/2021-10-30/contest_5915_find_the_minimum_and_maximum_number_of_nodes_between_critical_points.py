"""
- Identify indices of the critical points
- From the indices compute minDistance and maxDistance
"""


from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head

        idx = 0

        critical_points = []

        while curr and curr.next:

            idx += 1

            # print(f'  idx: {idx}')

            prev = curr
            curr = curr.next

            # Local maxima
            if prev.val < curr.val and curr.next is not None and curr.val > curr.next.val:
                critical_points.append(idx)
                # print(f'  appended local maxima')

            # Local minima
            if prev.val > curr.val and curr.next is not None and curr.val < curr.next.val:
                critical_points.append(idx)
                # print(f'  appended local minima')

            # idx += 1

        # print(f'critical_points: {critical_points}')

        if not critical_points or len(critical_points) == 1:
            return [-1, -1]

        min_so_far = critical_points[0]
        max_so_far = critical_points[0]

        min_distance = float('inf')
        max_distance = float('-inf')

        for num in critical_points[1:]:

            min_distance = min(num - max_so_far, min_distance)
            max_distance = max(num - min_so_far, max_distance)

            min_so_far = min(num, min_so_far)
            max_so_far = max(num, max_so_far)

        # print(f'min_distance: {min_distance}, max_distance: {max_distance}')

        return [min_distance, max_distance]


head = ListNode(3, ListNode(1))
head = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
head = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(7)))))))))
head = ListNode(2, ListNode(3, ListNode(3, ListNode(2))))
head = ListNode(2, ListNode(2, ListNode(1, ListNode(3))))
print(Solution().nodesBetweenCriticalPoints(head))
