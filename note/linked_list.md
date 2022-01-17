## Linked List

- `Singly linked list` contains value and a reference field to link to the next node, but no link to the previous node.
  - Cannot trace back the previous node, so the algorithm needs to store both current and previous nodes.
- `Doubly linked list` has `next` and `prev` field.
  - Delete is `O(1)` time and space unlike singly linked list, because no need to traverse.
- Two pointers technique (`prev` and `curr`, or `fast (hare)` and `slow (tortoise)`) often works for solution to 
  traverse the linked list.
  - Sometimes need `prev` because singly-linked list does not have a reference to the precedent node.
  - Check if a node is null before it calls the next field, otherwise it causes the null-pointer error.
  - Don't forget to define the end conditions in two pointers iteration loop.
- `Sentinel node` is a dummy pseudo head or tail node in linked list to standardize linked list algorithm, doesn't hold
  any meaningful data.
  - [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
- Benefit of linked list over array
  - In linked list, inserting an element is `O(1)` time because it only updates reference to next node. But in array,
    it takes `O(N)` time because it needs to move all elements after the inserted element.
  - If it needs to add or delete a node frequently, linked list is better.
  - If it needs to access an element by index, array is better.

| Action | Position | Array | Single linked list | Doubly linked list |
|--------|----------|-------|--------------------|--------------------|
| Access | By index | O(1) | O(N) | O(N) |
| Add | Before head | O(N) | **O(1)** | **O(1)** |
| Add | After given position | O(N) | **O(1)** | **O(1)** |
| Add | After tail | O(1) | O(N) | **O(1)** |
| Delete | Head | O(N) | **O(1)** | **O(1)** |
| Delete | Given position | O(N) | O(N) | **O(1)** |
| Delete | Tail | O(1) | O(N) | **O(1)** |
| Search | Given val | O(N) | O(N) | O(N) |

### Floyd's Tortoise and Hare (Floyd's cycle-finding algorithm)

- Detect cycle in linked list.
- Benefit of using this algorithm is
  1. Time is linear time `O(N)`
  2. Space is `O(1)` because it only uses two pointers to reference of linked lists.
- Algorithm
  - Find the intersection node by hare moving 2 nodes and tortoise moving 1 node.
  - Make two pointers
    - Pointer 1 starts from the intersection node
    - Pointer 2 starts from the head of linked list
    - Iterate both pointers one by one
    - Two pointers will be identical at the entrance of the cycly in the linked list.
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
- [Python code](https://github.com/yukikitayama/leetcode-python/blob/main/company/goldman-sachs/gs_142_linked_list_cycle_ii_2.py)
