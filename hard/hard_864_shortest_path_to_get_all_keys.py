from typing import List
import collections
import heapq


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        location = collections.defaultdict(tuple)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] not in ".#":
                    location[grid[r][c]] = (r, c)

        # print(location)

        # Distance from source to each point of interest
        def bfs_from(source):
            """source is point of interest character"""
            r, c = location[source]
            visited = [[False] * len(grid[0]) for _ in range(len(grid))]
            visited[r][c] = True
            # [(row, col, distance), ...]
            queue = collections.deque()
            queue.append((r, c, 0))
            dist = {}
            while queue:
                r, c, d = queue.popleft()

                # Record distance to each point of interest
                if grid[r][c] != "." and grid[r][c] != source:
                    dist[grid[r][c]] = d

                    # This is important!
                    # We only look for primitive segments, meaning no other points between points of interest
                    # once we find a point, stop exploring further, and try other primitive segments
                    continue

                for offset_r, offset_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_r = r + offset_r
                    next_c = c + offset_c
                    if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                        if grid[next_r][next_c] != "#" and not visited[next_r][next_c]:
                            visited[next_r][next_c] = True
                            queue.append((next_r, next_c, d + 1))

            return dist

        dists = {point_char: bfs_from(point_char) for point_char in location}

        # print(dists)

        # Each bit represents a key
        # e.g. when 2 keys, 2 ** 2 = 4 -> 100
        # by subtracting 1, 100 -> 011, 2 keys
        target_state = 2 ** sum(p.islower() for p in location) - 1

        # print(target_state, bin(target_state))

        # [(distance, point char, state?), ...]
        min_heap = []
        heapq.heappush(min_heap, (0, "@", 0))

        # If key isn't in the dict yet, it returns inf
        # If is a pair of point char and key collection state
        final_dist = collections.defaultdict(lambda: float("inf"))
        # Initialize with start point and no key collected
        final_dist["@", 0] = 0

        while min_heap:

            dist_so_far, place, curr_state = heapq.heappop(min_heap)

            # If previsouly found distance is shorter than current distance, no need to explore
            if final_dist[place, curr_state] < dist_so_far:
                continue

            # If collected all the keys
            if curr_state == target_state:
                return dist_so_far

            for destination, dist_to_next in dists[place].items():

                # print(destination, dist_to_next)

                next_state = curr_state

                # If next state is key
                if destination.islower():
                    # Collect key
                    next_state |= (1 << (ord(destination) - ord("a")))

                # If next state is lock, we need to check if we've collected the key
                elif destination.isupper():
                    # We can't visit next if we didn't collected the key before
                    if not (curr_state & (1 << (ord(destination) - ord("A")))):
                        continue

                if dist_so_far + dist_to_next < final_dist[destination, next_state]:
                    final_dist[destination, next_state] = dist_so_far + dist_to_next
                    heapq.heappush(min_heap, (dist_so_far + dist_to_next, destination, next_state))

        return -1