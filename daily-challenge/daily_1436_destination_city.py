from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        sources = set()
        destinations = set()

        for source, destination in paths:
            sources.add(source)
            destinations.add(destination)

        for destination in destinations:
            if destination not in sources:
                return destination


if __name__ == "__main__":
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(Solution().destCity(paths))


