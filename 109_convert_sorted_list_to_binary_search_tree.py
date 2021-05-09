
TESTCASE = [-10, -3, 0, 5, 9]


# Singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


head = ListNode(val=-3, next=ListNode(val=0, next=ListNode(val=5, next=None)))

prev = None
slow = head
fast = head

if fast:
    print('if')
    print(fast)

