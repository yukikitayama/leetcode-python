from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        ans = []

        # Time O(N^2) because for each person, insertion takes O(N) to move elements in the list
        for person in people:

            # Python LIST.insert(index, element)
            ans.insert(person[1], person)

        return ans


if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(Solution().reconstructQueue(people))
