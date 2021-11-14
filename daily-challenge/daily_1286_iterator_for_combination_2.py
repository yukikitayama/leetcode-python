"""
- Bitmasking precomputation
"""


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.n = len(characters)
        self.k = combinationLength

        # e.g. characters: 'abc', n: 3, range(8), 8 is 1000
        # So 8 (1000) can cover 3 1-bits
        # 0 to 7 can cover all the patterns of 3 1-bits,
        # 0: 000, 1: 001, 2: 010, 3: 011, ..., 7: 111
        for bitmask in range(1 << self.n):
            if bin(bitmask).count('1') == self.k:
                curr = [characters[i] for i in range(self.n) if bitmask & (1 << self.n - 1 - i)]
                curr = ''.join(curr)
                # Append by lexicographical descending order
                # because 1-bit are filled from the right
                self.combinations.append(curr)

                # print(f'  curr: {curr}')

    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations


itr = CombinationIterator('abc', 2)
print(''.join(itr.next()))
print(''.join(itr.next()))
