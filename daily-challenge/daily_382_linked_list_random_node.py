from typing import Optional
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        # Assume there is at least one element in the linked list
        scope = 1
        # Ret is 0 as the initial index
        ret = 0

        curr = self.head
        while curr:
            if random.random() < (1 / scope):
                ret = curr.val
            curr = curr.next
            scope += 1

        return ret


class Solution1:
    def __init__(self, head: Optional[ListNode]):
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.range)


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3)))
    obj = Solution(head)
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
