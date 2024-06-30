from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertex_sets = set()
        for u, v in edges:
            if u in vertex_sets:
                return u
            if v in vertex_sets:
                return v
            vertex_sets.add(u)
            vertex_sets.add(v)