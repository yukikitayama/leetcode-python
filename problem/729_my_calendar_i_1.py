class Node:
    __slots__ = ['start', 'end', 'left', 'right']

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, node: 'Node') -> bool:
        # Insert after the middle node
        if node.start >= self.end:
            # If empty after the middle node
            if not self.right:
                self.right = node
                return True
            # If not, at the side after the middle node,
            # try to find places to be able to insert
            return self.right.insert(node)

        # Insert before the middle node
        elif node.end <= self.start:
            # If empty before the middle node
            if not self.left:
                self.left = node
                return True
            # If not, at the side before the middle node,
            # try to find places to be able to insert
            return self.left.insert(node)
        else:
            return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> int:
        # Very first case
        if self.root is None:
            self.root = Node(start, end)
            return True
        # Otherwise
        return self.root.insert(Node(start, end))


test = [[10, 20], [15, 25], [20, 30]]
obj = MyCalendar()
for start, end in test:
    print(obj.book(start, end))
