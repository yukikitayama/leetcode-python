"""
- Bitmasking next combination
"""


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = combinationLength
        self.characters = characters
        # Generate the first bitmask
        # e.g. characters: 'abc', k: 2, n: 3, 1 << n: '1000' = 8
        # n - k: 1, 1 << 1: '10' = 2, 8 - 2: 6 = '110'
        self.b = (1 << self.n) - (1 << self.n - self.k)

        # print(f'self.b: {self.b}, bin(self.b): {bin(self.b)}, '
        #       f'bin(1 << self.n): {bin(1 << self.n)}, '
        #       f'bin(1 << self.n - self.k): {bin(1 << self.n - self.k)}')

    def next(self) -> str:
        curr = [self.characters[i] for i in range(self.n) if self.b & (1 << self.n - 1 - i)]

        # Next
        self.b -= 1
        while self.b > 0 and bin(self.b).count('1') != self.k:
            self.b -= 1
        return ''.join(curr)

    def hasNext(self) -> bool:
        return self.b > 0


itr = CombinationIterator('abc', 2)
# print(''.join(itr.next()))
# print(''.join(itr.next()))
