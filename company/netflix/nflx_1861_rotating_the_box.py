from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        for row in box:
            # Since stone fell by gravity, we process from the end in each row
            i = len(row) - 1

            for j in range(len(row) - 1, -1, -1):

                # If obstacle, stone cannot pass this point
                if row[j] == '*':
                    i = j - 1

                # If stone, we swap it with empty space to move
                elif row[j] == '#':
                    row[i], row[j] = row[j], row[i]

                    # Update next available position
                    i -= 1

        ans = []
        for row in zip(*box[::-1]):
            ans.append(list(row))

        return ans


if __name__ == '__main__':
    box = [["#", ".", "*", "."],
           ["#", "#", "*", "."]]
    ans = Solution().rotateTheBox(box)
    for row in ans:
        print(row)
