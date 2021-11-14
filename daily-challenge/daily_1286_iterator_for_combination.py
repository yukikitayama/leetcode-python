"""
- Backtracking
"""


import collections


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = collections.deque([])

        def backtracking(index, curr):

            if len(curr) == combinationLength:
                combination = ''.join(curr)
                self.combinations.append(combination)
                return

            for i in range(index, len(characters)):
                curr.append(characters[i])
                backtracking(i + 1, curr)
                curr.pop()

        backtracking(0, [])

        # The given characters is sorted distinct so backtracking gives us the lexicographical order
        print(self.combinations)

    def next(self) -> str:
        return self.combinations.popleft()

    def hasNext(self) -> bool:
        return len(self.combinations) != 0


itr = CombinationIterator('abc', 2)
print(''.join(itr.next()))
print(''.join(itr.next()))
