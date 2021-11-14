from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(prev, curr, length):
            for _ in range(length):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return curr

        curr = head
        count = 1
        while curr:

            print(f'  count: {count}')
            print(f'  curr.val: {curr.val}')

            if count % 2 == 1:
                curr = curr.next
                count += 1

            elif count % 2 == 0:
                curr = reverse(curr, curr.next, count)
                count += count + 1



# head = ListNode(7, ListNode(3, ListNode(8, ListNode(4))))
head = ListNode(5, ListNode(2, ListNode(6, ListNode(3, ListNode(9, ListNode(1, ListNode(7, ListNode(3, ListNode(8, ListNode(4))))))))))
ans = Solution().reverseEvenLengthGroups(head)
print(ans)



