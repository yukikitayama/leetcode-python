from typing import List
import collections


class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        # Find all possible bottom row combination
        combos = []

        def get_combos(cur, cur_sum):
            """

            :param cur: current combination of bricks
            :param cur_sum: current width
            :return:
            """
            nonlocal combos
            nonlocal width

            # If exceed, fail, terminate
            if cur_sum > width:
                return

            # If success, add to combination
            if cur_sum == width:
                combos.append(tuple(cur))
                return

            for brick in bricks:
                get_combos(cur + [brick], cur_sum + brick)

        get_combos([], 0)

        print(combos)

        # Make an adjacency list for {combo: [possible_neighbor_row]}
        d = collections.defaultdict(list)

        # For each combo, find its possible neighbor row
        for i, combo in enumerate(combos):

            print(f'i: {i}')

            s = set()
            cur = 0

            # [:-1] for except the last one
            # because sturdy doesn't care the end of the wall
            for val in combo[:-1]:
                print(f'    val: {val}')
                s.add(cur := cur + val)

            print(f's: {s}')

            for j, nei in enumerate(combos):
                cur = 0
                for val in nei[:-1]:
                    cur + val
                    if cur in s:
                        break
                else:
                    d[combo].append(nei)


if __name__ == '__main__':
    height = 2
    width = 3
    bricks = [1, 2]
    print(Solution().buildWall(height, width, bricks))
