"""
"""


from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        for n in range(1001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(n, k)

        # print(f'n: {n}, k: {k}, width: {width}, remainder: {remainder}')

        ans = []
        cur = head

        for i in range(k):

            # print(f'i: {i}')

            root = cur

            # -1 because we don't have dummy head anymore
            # n: 10, k: 3, width: 3, remainder: 1
            # i: 0, width + int(i < remainder) - 1: 3 + 1 - 1 = 3
            # i needs to have length 4, but the first item was made out of for loop by root = cur above
            # so minus 1
            for j in range(width + int(i < remainder) - 1):

                # print(f'  j: {j}')

                if cur:
                    cur = cur.next

            if cur:
                # Go to the next root
                # Temporarily save the next linked list
                tmp = cur.next
                # current list node end needs to have None
                cur.next = None
                # Get the head of the next linked list in answer list
                cur = tmp

                # cur.next, cur = None, cur.next

            ans.append(root)

        return ans


# head = ListNode(1, ListNode(2, ListNode(3)))
# k = 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
k = 3
ans = Solution().splitListToParts(head, k)
for head in ans:
    while head:
        print(head.val, end=', ')
        head = head.next
    print()
    print()





