"""
- BFS

- Wrong
"""


from typing import List
import collections


class Solution:
    def __init__(self):
        self.flight_map = None
        self.result = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flight_map = collections.defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flight_map[origin].append(dest)

        print(f'flightMap: {self.flight_map}')

        for origin, itinerary in self.flight_map.items():

            itinerary.sort(reverse=True)

        self.DFS('JFK')
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flight_map[origin]
        while destList:
            nextDest = destList.pop()

            print(f'  nextDest: {nextDest}')

            self.DFS(nextDest)

        self.result.append(origin)


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","SFO"],["SFO","ATL"],["SFO","BOS"],["SFO","LHR"],["ATL","BOS"],["BOS","LHR"],["LHR","BOS"],["BOS","ATL"]]
print(Solution().findItinerary(tickets))

