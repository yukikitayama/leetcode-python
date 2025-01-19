"""
[1,1,1,0,0,0,0,0,0],
[1,0,1,0,1,1,1,1,1],
[1,1,1,0,0,0,0,0,0]
First build to the right, and build to the expanded left

Ans
  simulation
"""

from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < len(isInfected) and 0 <= nc < len(isInfected[0]):
                    yield nr, nc

        def dfs(r, c):
            if (r, c) not in seen:
                seen.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in neighbors(r, c):
                    if isInfected[nr][nc] == 1:
                        dfs(nr, nc)
                    elif isInfected[nr][nc] == 0:
                        frontiers[-1].add((nr, nc))
                        perimeters[-1] += 1

        ans = 0

        while True:

            seen = set()
            regions = []
            frontiers = []
            perimeters = []

            for r, row in enumerate(isInfected):
                for c, val in enumerate(row):

                    if val == 1 and (r, c) not in seen:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)

                        dfs(r, c)

            if not regions:
                break

            # Add perimeter of the region which will infect the most
            triage_index = frontiers.index(max(frontiers, key=len))
            ans += perimeters[triage_index]

            # Triage the most infectious region
            for i, reg in enumerate(regions):
                if i == triage_index:
                    for r, c in reg:
                        isInfected[r][c] = -1

                # Infect
                else:
                    for r, c in reg:
                        for nr, nc in neighbors(r, c):
                            if isInfected[nr][nc] == 0:
                                isInfected[nr][nc] = 1

        return ans