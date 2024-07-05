from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        # Edge case
        if not head:
            return [-1, -1]
        if head and not head.next:
            return [-1, -1]
        if head and head.next and not head.next:
            return [-1, -1]

        prev = head
        curr = head.next
        next_ = head.next.next
        curr_pos = 2
        first_pos = None
        prev_pos = None
        max_distance = float("-inf")
        min_distance = float("inf")

        while next_:
            if prev.val < curr.val > next_.val or prev.val > curr.val < next_.val:
                if first_pos is not None:

                    min_distance = min(
                        min_distance,
                        curr_pos - prev_pos
                    )

                    max_distance = max(
                        max_distance,
                        curr_pos - first_pos
                    )

                    prev_pos = curr_pos

                elif first_pos is None:
                    first_pos = curr_pos
                    prev_pos = curr_pos

            prev = curr
            curr = next_
            next_ = next_.next
            curr_pos += 1

        if max_distance == float("-inf") or min_distance == float("inf"):
            return [-1, -1]

        return [min_distance, max_distance]

    def nodesBetweenCriticalPoints1(self, head: Optional[ListNode]) -> List[int]:

        # Edge case
        if not head:
            return [-1, -1]
        if head and not head.next:
            return [-1, -1]
        if head and head.next and not head.next:
            return [-1, -1]

        prev = head
        curr = head.next
        next_ = head.next.next
        positions = []
        curr_pos = 2

        while next_:
            if prev.val < curr.val > next_.val or prev.val > curr.val < next_.val:
                positions.append(curr_pos)

            prev = curr
            curr = next_
            next_ = next_.next
            curr_pos += 1

        if len(positions) <= 1:
            return [-1, -1]

        max_distance = positions[-1] - positions[0]
        min_distance = float("inf")
        for i in range(1, len(positions)):
            min_distance = min(
                min_distance,
                positions[i] - positions[i - 1]
            )

        return [min_distance, max_distance]