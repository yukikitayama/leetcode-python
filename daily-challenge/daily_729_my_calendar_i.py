"""
- If existing end <= current start, can book
- If current end <= existing start, can book
"""


class Node:
    def __init__(self, start, end):
        self.start = start,
        self.end = end
        self.left = None
        self.right = None

    def insert(self, node):
        # Book after the existing schedule
        if self.end <= node.start:
            # If no schedule after this
            if not self.right:
                self.right = node
                return True
            # If there's schedule after this, recursively check
            return self.right.insert(node)

        # Book before the existing schedule
        elif node.end <= self.start:
            # If no schedule before this
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)

        # Otherwise schedules conflict
        else:
            return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))




