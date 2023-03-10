import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        ans = 0
        curr = self.head

        while curr:
            if random.random() < 1 / scope:
                ans = curr.val

            curr = curr.next
            scope += 1

        return ans


class Solution1:
    def __init__(self, head: ListNode):
        self.array = []
        while head:
            self.array.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        # random.random() has inclusive start and exclusive end
        i = int(random.random() * len(self.array))
        return self.array[i]

