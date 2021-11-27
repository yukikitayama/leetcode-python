"""
- Initialize stack
- Initialize hashmap
- push()
  - increment the hashmap
- pop()
  - decrement the hashmap
  - Search from the top of the stack
"""


import collections


class FreqStack:
    def __init__(self):
        self.freq = collections.Counter()
        # When we pop the most frequent element and there's a tie,
        # we need to pop the recent one.
        # We make also a stack for the elements with the same frequency,
        # so if we take group[-1], it's the recent element
        # Each element will exist in every list of each frequency
        # e.g. When 5 frequency changed from 1 to 2
        # {1: [5], 2: [5]}. We still have 5 in Key 1
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f

        if f > self.maxfreq:
            self.maxfreq = f

        self.group[f].append(val)

        print(f'push():')
        print(f'  self.freq: {self.freq}')
        print(f'  self.group: {self.group}')
        print(f'  self.maxfreq: {self.maxfreq}')

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1

        # If the current frequency list becomes empty
        # most frequent elements are gone, so decrement max frequency too
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        print(f'pop():')
        print(f'  self.freq: {self.freq}')
        print(f'  self.group: {self.group}')
        print(f'  self.maxfreq: {self.maxfreq}')

        return x


obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())


