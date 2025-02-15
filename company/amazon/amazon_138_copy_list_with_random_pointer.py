"""
Hashmap
  k: original node
  v: copy node

curr_original from head
create copy_head and curr_copy

while curr_original is not none
  create copy next from original next
  add to hashmap
  add copy next to curr_copy
  random
    if random in hashmap
      copy random is value of the hashmap with original random as key

  iterate next
    assgin original next to curr_original
    assign copy next to curr_copy
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # Interweave next
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Assign random
        curr = head
        while curr:
            # curr.next is copy of next
            # curr.random.next is copy of random
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        # Unweave
        curr_old = head
        curr_new = head.next
        head_new = head.next
        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next
        return head_new

    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy_head = Node(x=head.val)

        original_to_copy = {head: copy_head}

        def clone(node):
            if node:
                if node in original_to_copy:
                    return original_to_copy[node]
                else:
                    original_to_copy[node] = Node(node.val)
                    return original_to_copy[node]
            else:
                return None

        curr_original = head
        curr_copy = copy_head

        while curr_original:
            curr_copy.next = clone(curr_original.next)
            curr_copy.random = clone(curr_original.random)

            # Iterate
            curr_original = curr_original.next
            curr_copy = curr_copy.next

        return copy_head

    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy_head = Node(x=head.val)

        original_to_copy = {head: copy_head}

        curr_original = head
        curr_copy = copy_head

        while curr_original:

            next_original = curr_original.next
            random_original = curr_original.random

            # Next
            if next_original is None:
                curr_copy.next = None
            elif next_original not in original_to_copy:
                next_copy = Node(next_original.val)
                original_to_copy[next_original] = next_copy
                curr_copy.next = next_copy
            else:
                curr_copy.next = original_to_copy[next_original]

            # Random
            if random_original is None:
                curr_copy.random = None
            elif random_original not in original_to_copy:
                random_copy = Node(random_original.val)
                original_to_copy[random_original] = random_copy
                curr_copy.random = random_copy
            else:
                curr_copy.random = original_to_copy[random_original]

            # Iterate
            curr_original = curr_original.next
            curr_copy = curr_copy.next

        return copy_head