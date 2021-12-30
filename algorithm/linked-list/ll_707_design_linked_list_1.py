class SinglyListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.get_node(index)
        if not curr:
            return -1
        else:
            return curr.val

    def addAtHead(self, val: int) -> None:
        curr = SinglyListNode(val)
        curr.next = self.head
        self.head = curr

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
        else:
            prev = self.get_tail()
            curr = SinglyListNode(val)
            prev.next = curr

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            prev = self.get_node(index - 1)

            # If index is greater than the length of linked list, invalid
            if not prev:
                return

            curr = SinglyListNode(val)
            next = prev.next
            prev.next = curr
            curr.next = next

    def deleteAtIndex(self, index: int) -> None:
        curr = self.get_node(index)

        if not curr:
            return

        else:
            next = curr.next

            # If deleting the head
            if index == 0:
                self.head = next

            else:
                prev = self.get_node(index - 1)
                prev.next = next

    def get_node(self, index) -> SinglyListNode:
        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        return curr

    def get_tail(self) -> SinglyListNode:
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        return curr


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    print(obj.get(0))
    print(obj.get(1))
    print(obj.get(2))
    # 1 -> 2 -> 3
    obj.deleteAtIndex(1)
    # 1 -> 3
    print(obj.get(1))
    # 3
