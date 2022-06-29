from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        ans = []

        for person in people:
            ans.insert(person[1], person)
            # print(f'ans: {ans}')

        return ans


if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    # [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    print(Solution().reconstructQueue(people))
