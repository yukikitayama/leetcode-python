"""
- Initialize empty answer list with size k
- We don't know the length of linked list, so we don't know what length each linked list will have
  in each element of the answer list
- O(n) to scan to know the size of linked list, and calculate the size of each element in the answer list
  - n: 3, k: 3, n / k: 1
  - n: 4, k: 3, n / k: quotient 1 and remainder 1, the first element will have additional 1
    - base size n / k, and the first element has n / k + n % k
  - n: 5, k: 3, n / k: quotient: 1 and remainder: 2, the first n % k heads have additional 1
- and O(n) to iterate each list node and append it to answer list
"""


from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head

        # 1001 comes from constrains
        for n in range(1001):
            if not cur:
                break
            cur = cur.next

        # divmod(numerator, denominator) returns (quotient, remainder)
        # width is the size of each element in the answer list
        width, remainder = divmod(n, k)

        ans = []
        cur = head

        for i in range(k):
            each_dummy_head = ListNode(None)
            each_iterate_node = each_dummy_head

            # remainder: 2, first two heads in answer list need to have one additional node than others
            # i starts from 0, i: 0, i < remainder: True, i: 1, i < remainder: True, i: 2, i < remainder: False
            # int(True): 1, with the below boolean, it can add 1 depending on which element in the answer list
            for j in range(width + int(i < remainder)):
                node = ListNode(cur.val)
                each_iterate_node.next = node
                each_iterate_node = each_iterate_node.next

                if cur:
                    cur = cur.next

            ans.append(each_dummy_head.next)

        return ans


head = ListNode(1, ListNode(2, ListNode(3)))
k = 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
k = 3
ans = Solution().splitListToParts(head, k)
for head in ans:
    while head:
        print(head.val, end=', ')
        head = head.next
    print()
    print()





