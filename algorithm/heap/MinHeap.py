class MinHeap:
    def __init__(self, size):
        # Initialize the heap size
        self.heap_size = size
        # +1 for convenience of index calculation
        # Element at index 0 is not used
        self.min_heap = [0] * (size + 1)
        # Size of actually contained elements in the array
        self.real_size = 0

    def insert(self, element):
        self.real_size += 1

        # It does not allow to add an element more than the heap size
        if self.real_size > self.heap_size:
            print('Add too many elements!')
            self.real_size -= 1
            return

        # Insert a new element at the bottom rightmost
        self.min_heap[self.real_size] = element

        # Exchange it with the parent to satisfy heap condition
        index = self.real_size
        parent = index // 2
        while self.min_heap[index] < self.min_heap[parent] and index > 1:
            self.min_heap[parent], self.min_heap[index] = self.min_heap[index], self.min_heap[parent]
            index = parent
            parent = index // 2

    def delete(self):
        if self.real_size < 1:
            print('Do not have any element!')
            return

        else:
            # Get top element
            remove_element = self.min_heap[1]

            # Move the bottom right most element to the top
            self.min_heap[1] = self.min_heap[self.real_size]
            self.real_size -= 1

            # Exchange the new top with child to satisfy heap condition
            index = 1
            while index < self.real_size and index <= self.real_size // 2:
                left = index * 2
                right = index * 2 + 1
                if self.min_heap[index] > self.min_heap[left] or self.min_heap[index] > self.min_heap[right]:
                    if self.min_heap[left] < self.min_heap[right]:
                        self.min_heap[left], self.min_heap[index] = self.min_heap[index], self.min_heap[left]
                        index = left
                    else:
                        self.min_heap[right], self.min_heap[index] = self.min_heap[index], self.min_heap[right]
                        index = right
                else:
                    break

            return remove_element
