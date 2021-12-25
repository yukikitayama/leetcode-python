from typing import List
import collections


class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flight_map = collections.defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flight_map[origin].append(dest)

        for origin, itinerary in self.flight_map.items():
            # Reverse because it pops a vertex from the end
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS('JFK')
        return self.result[::-1]

    def DFS(self, origin):
        dest_list = self.flight_map[origin]

        while dest_list:
            next_dest = dest_list.pop()
            self.DFS(next_dest)

        self.result.append(origin)


class Solution1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flight_map = collections.defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flight_map[origin].append(dest)

        self.visit_bit_map = {}

        for origin, itinerary in self.flight_map.items():
            itinerary.sort()
            self.visit_bit_map[origin] = [False] * len(itinerary)

        # print(self.flight_map)
        # print(self.visit_bit_map)

        self.flights = len(tickets)
        self.result = []
        route = ['JFK']
        self.backtracking('JFK', route)
        return self.result

    def backtracking(self, origin, route):
        if len(route) == self.flights + 1:
            self.result = route
            return True

        for i, next_dest in enumerate(self.flight_map[origin]):
            if not self.visit_bit_map[origin][i]:
                self.visit_bit_map[origin][i] = True
                ret = self.backtracking(next_dest, route + [next_dest])
                self.visit_bit_map[origin][i] = False
                if ret:
                    return True

        return False


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(Solution().findItinerary(tickets))

