"""
BFS
  Dijkstra
Impossible
  cycle, visit the previously visited cell
How to find the next cell

ball: [0,4]
hole: [3, 5]
[
    [0,0,0,0,B,0,0],
    [0,0,1,0,0,1,0],
    [0,0,0,0,1,0,0],
    [0,0,0,0,0,H,1]
]
exp: dldr

ball: [0, 4]
hole: [2, 0]
[
    [0,0,0,0,B,0,0],
    [0,0,1,0,0,1,0],
    [H,0,0,0,1,0,0],
    [0,0,0,0,0,0,1]
]
exp: ld

ball: [2, 4]
hole: [7, 6]
[
    [0,1,0,0,1,0,0,1,0,0],
    [0,0,1,0,0,1,0,0,1,0],
    [0,0,0,0,B,0,1,0,0,1],
    [0,0,0,0,0,0,1,0,0,1],
    [0,1,0,0,1,0,0,1,0,0],
    [0,0,1,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [1,0,0,1,0,0,H,0,0,1],
    [0,1,0,0,1,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,1,0]
]
exp: "drdrdrdldl", 13
out: "rdrdrdldl", 13
"""

from typing import List
import heapq


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:

        def find_neighbors(r, c):
            res = []
            for offset_r, offset_c, direction in [(0, -1, "l"), (-1, 0, "u"), (0, 1, "r"), (1, 0, "d")]:
                curr_r = r
                curr_c = c
                dist = 0

                while 0 <= curr_r + offset_r < len(maze) and 0 <= curr_c + offset_c < len(maze[0]) and \
                        maze[curr_r + offset_r][curr_c + offset_c] == 0:
                    curr_r += offset_r
                    curr_c += offset_c
                    dist += 1

                    # If in the middle, hole is found
                    if curr_r == hole[0] and curr_c == hole[1]:
                        break

                if (curr_r, curr_c) != (r, c):
                    res.append([curr_r, curr_c, dist, direction])

            return res

        min_heap = []
        heapq.heappush(min_heap, (0, "", ball[0], ball[1]))
        visited = set()

        while min_heap:

            d, chars, r, c = heapq.heappop(min_heap)

            # In case visiting the same cell with the same distance
            # we wannt filter out lexicographically bigger chars
            # Above heappop gives us the same cell with same distance earlier than current
            # so we can filter out
            if (r, c) in visited:
                continue

            if (r, c) == (hole[0], hole[1]):
                return chars

            # By adding row col to hashset hear, below heappush allows to have duplicated row col pairs in min heap but with different chars
            # Ok to have duplicates because we wanna explore lexicographically smaller
            # But this hashset add and the above hashset in continue can filter out lexicographically bigger
            visited.add((r, c))

            for next_r, next_c, next_distance, next_direction in find_neighbors(r, c):
                heapq.heappush(min_heap, (d + next_distance, chars + next_direction, next_r, next_c))

        return "impossible"

    def findShortestWay2(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:

        def find_neighbors(r, c):
            res = []
            for offset_r, offset_c, direction in [(0, -1, "l"), (-1, 0, "u"), (0, 1, "r"), (1, 0, "d")]:
                curr_r = r
                curr_c = c
                found_hole = False

                while 0 <= curr_r + offset_r < len(maze) and 0 <= curr_c + offset_c < len(maze[0]) and \
                        maze[curr_r + offset_r][curr_c + offset_c] == 0:
                    curr_r += offset_r
                    curr_c += offset_c

                    # If in the middle, hole is found
                    if curr_r == hole[0] and curr_c == hole[1]:
                        res.append([curr_r, curr_c, direction])
                        found_hole = True

                if not found_hole and (curr_r, curr_c) != (r, c):
                    res.append([curr_r, curr_c, direction])

            return res

        # print(find_neighbors(ball[0], ball[1]))

        def compute_distance(r1, c1, r2, c2):
            return abs(r1 - r2) + abs(c1 - c2)

        # [(distance, directions string, r, c)]
        min_heap = []
        heapq.heappush(min_heap, (0, "", ball[0], ball[1]))
        visited = set()

        while min_heap:

            d, chars, r, c = heapq.heappop(min_heap)

            print(f"d: {d}, chars: {chars}, r: {r}, c: {c}")

            if (r, c) in visited:
                print("skip")
                continue

            if (r, c) == (hole[0], hole[1]):
                # print(f"Hole, chars: {chars}")
                return chars

            visited.add((r, c))

            for next_r, next_c, next_direction in find_neighbors(r, c):
                next_distance = compute_distance(r, c, next_r, next_c)
                heapq.heappush(min_heap, (d + next_distance, chars + next_direction, next_r, next_c))

        return "impossible"

    def findShortestWay1(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:

        def find_neighbors(r, c):
            res = []
            for offset_r, offset_c, direction in [(0, -1, "l"), (-1, 0, "u"), (0, 1, "r"), (1, 0, "d")]:
                curr_r = r
                curr_c = c
                found_hole = False

                while 0 <= curr_r + offset_r < len(maze) and 0 <= curr_c + offset_c < len(maze[0]) and \
                        maze[curr_r + offset_r][curr_c + offset_c] == 0:
                    curr_r += offset_r
                    curr_c += offset_c

                    # If in the middle, hole is found
                    if curr_r == hole[0] and curr_c == hole[1]:
                        res.append([curr_r, curr_c, direction])
                        found_hole = True

                if not found_hole and (curr_r, curr_c) != (r, c):
                    res.append([curr_r, curr_c, direction])

            return res

        # print(find_neighbors(ball[0], ball[1]))

        def compute_distance(r1, c1, r2, c2):
            return abs(r1 - r2) + abs(c1 - c2)

        # [(distance, directions string, r, c)]
        min_heap = []
        heapq.heappush(min_heap, (0, "", ball[0], ball[1]))
        visited = set()
        visited.add((ball[0], ball[1]))
        min_so_far = float("inf")
        ans = []

        while min_heap:

            d, chars, r, c = heapq.heappop(min_heap)

            print(f"d: {d}, chars: {chars}, r: {r}, c: {c}")

            if d < min_so_far and (r, c) == (hole[0], hole[1]):
                print(f"Hole, chars: {chars}")
                ans = [chars]
                min_so_far = min(min_so_far, d)
            elif d <= min_so_far and (r, c) == (hole[0], hole[1]):
                print(f"Hole, chars: {chars}")
                ans.append(chars)
                min_so_far = min(min_so_far, d)

            for next_r, next_c, next_direction in find_neighbors(r, c):
                if (next_r, next_c) not in visited:
                    next_distance = compute_distance(r, c, next_r, next_c)
                    heapq.heappush(min_heap, (d + next_distance, chars + next_direction, next_r, next_c))
                    if (next_r, next_c) != (hole[0], hole[1]):
                        visited.add((next_r, next_c))

        # print(ans)

        if not ans:
            return "impossible"
        elif len(ans) == 1:
            return ans[0]
        elif len(ans) > 1:
            ans.sort()
            return ans[0]

