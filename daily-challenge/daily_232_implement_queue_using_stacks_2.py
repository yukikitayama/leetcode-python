"""
push
  append to list
  if empty, save the value to front attribute
pop
  pop everything into another list except last one
  save the second last to front attribute
peek
  return front
empty
  return if length of list is 0
"""


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            return self.front

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    print(queue.stack)
    queue.push(2)
    print(queue.stack)
    print(queue.peek())
    print(queue.pop())
    print(f"front: {queue.front}")
    print(f"stack: {queue.stack}")
    print(queue.empty())
