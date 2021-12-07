"""
- Start: 7:02
- End: 7:09
- Solved: 1
- Optimized: 0
- Saw solution: 0
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_num_str = ''
        while head:
            bin_num_str += str(head.val)
            head = head.next
        return int(bin_num_str, 2)


if __name__ == '__main__':
    head = ListNode(1, ListNode(0, ListNode(1)))
    print(Solution().getDecimalValue(head))
