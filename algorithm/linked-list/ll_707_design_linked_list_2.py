class DoublyListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get_node(self, index):
        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        return curr

    def get_tail(self):
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        return curr

    def get(self, index):
        curr = self.get_node(index)
        return curr.val if curr else -1

    def addAtHead(self, val):
        curr = DoublyListNode(val)
        curr.next = self.head
        if self.head:
            self.head.prev = curr
        self.head = curr

    def addAtTail(self, val):
        if not self.head:
            self.addAtHead(val)
        else:
            prev = self.get_tail()
            curr = DoublyListNode(val)
            prev.next = curr
            curr.prev = prev

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
        else:
            # get_node() returns None if head is None or index exceeds the length of linked list
            prev = self.get_node(index - 1)
            if not prev:
                return
            curr = DoublyListNode(val)
            next = prev.next
            curr.prev = prev
            curr.next = next
            prev.next = curr
            if next:
                next.prev = curr

    def deleteAtIndex(self, index):
        curr = self.get_node(index)
        if not curr:
            return
        prev = curr.prev
        next = curr.next
        if prev:
            prev.next = next
        # Otherwise deleting the head
        else:
            self.head = next

        if next:
            next.prev = prev


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(1)
    print(obj.head.val)
    obj.addAtTail(3)
    print(obj.head.next.val)
    obj.addAtIndex(1, 2)
    print(obj.head.val)
    print(obj.head.next.val)
    print(obj.head.next.next.val)
    print(obj.get(1))