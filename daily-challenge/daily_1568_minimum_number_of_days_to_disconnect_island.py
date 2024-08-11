from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        """I don't understand Tarjan's algorithm"""
        rows = len(grid)
        cols = len(grid[0])

        ap_info = {
            "has_articulation_point": False,
            "time": 0
        }
        # Time when a cell is first discovered
        discovery_time = [[-1] * cols for _ in range(rows)]
        # Lowest discovery time reachable from the subtree rooted at this cell
        lowest_reachable = [[-1] * cols for _ in range(rows)]
        # Parent of each cell in DFS tree
        parent_cell = [[-1] * cols for _ in range(rows)]

        def find_articulation_points(r, c):
            discovery_time[r][c] = ap_info["time"]

            ap_info["time"] += 1

            lowest_reachable[r][c] = discovery_time[r][c]

            children = 0

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r = r + dr
                new_c = c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:

                    # If not visited yet
                    if discovery_time[new_r][new_c] == -1:
                        children += 1

                        parent_idx = r * cols + c
                        parent_cell[new_r][new_c] = parent_idx

                        find_articulation_points(new_r, new_c)

                        lowest_reachable[r][c] = min(
                            lowest_reachable[r][c],
                            lowest_reachable[new_r][new_c]
                        )

                        if lowest_reachable[new_r][new_c] >= discovery_time[r][c] and parent_cell[r][c] != -1:
                            ap_info["has_articulation_point"] = True

                    elif new_r * cols + new_c != parent_cell[r][c]:
                        lowest_reachable[r][c] = min(
                            lowest_reachable[r][c],
                            discovery_time[new_r][new_c]
                        )

            if parent_cell[r][c] == -1 and children > 1:
                ap_info["has_articulation_point"] = True

        land_cells = 0
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    land_cells += 1

                    # If not visited yet
                    if discovery_time[r][c] == -1:
                        find_articulation_points(r, c)

                        island_count += 1

        if island_count == 0 or island_count >= 2:
            return 0
        if land_cells == 1:
            return 1
        if ap_info["has_articulation_point"]:
            return 1
        return 2

    def minDays1(self, grid: List[List[int]]) -> int:

        def count_islands():
            visited = set()
            count = 0
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        explore(r, c, visited)
                        count += 1
            return count

        def explore(r, c, visited):
            if (
                    r < 0 or r >= len(grid)
                    or c < 0 or c >= len(grid[0])
                    or grid[r][c] == 0
                    or (r, c) in visited
            ):
                return
            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                explore(r + dr, c + dc, visited)

        # Edge case: Already disconnected
        if count_islands() != 1:
            return 0

        # Flood fill
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    # Try flood fill for each flip
                    if count_islands() != 1:
                        return 1
                    # Backtrack
                    grid[r][c] = 1

        # Thinnest cross-section at most 2
        return 2