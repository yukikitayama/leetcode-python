import collections

# This makes a list of list, [[0, None]]
queue = collections.deque()
queue.append([0, None])
print(queue)

# If you wanna make a list [0, None]
queue = collections.deque([0, None])
print(queue)

# Or
queue = collections.deque()
queue.append(0)
queue.append(None)
print(queue)