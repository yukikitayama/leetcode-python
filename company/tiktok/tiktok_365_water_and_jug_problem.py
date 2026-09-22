class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False

        stack = [(0, 0)]
        visited = set()

        while stack:

            curr_x, curr_y = stack.pop()

            if curr_x + curr_y == target:
                return True

            if (curr_x, curr_y) in visited:
                continue

            visited.add((curr_x, curr_y))

            stack.extend([
                # Fill x jug completely with water
                (x, curr_y),
                # Fill y jug completely with water
                (curr_x, y),
                # Completely empty x jug
                (0, curr_y),
                # Completely empty y jug
                (curr_x, 0)
            ])

            # Pour water from x jug into y jug until y jug is full, or x jug is empty
            w = min(curr_x, y - curr_y)
            stack.append((curr_x - w, curr_y + w))

            # Pour water from y jug into x jug until x jug is full, or y jug is empty
            # e.g., curr_x: 0, curr_y: 5, x: 3, w: 3
            w = min(curr_y, x - curr_x)
            stack.append((curr_x + w, curr_y - w))

        return False