from typing import List
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(collections.defaultdict)

        for source, destination, time in times:
            graph[source][destination] = time

        # Min heap: [(total time, node), ...]
        heap = [(0, k)]
        heapq.heapify(heap)

        # ?
        dist = {}

        while heap:

            time, curr = heapq.heappop(heap)

            if curr not in dist:
                dist[curr] = time

                for neighbor in graph[curr]:
                    heapq.heappush(heap, (time + graph[curr][neighbor], neighbor))

            # print(f'  curr: {curr}, dist: {dist}')

        # print(f'dist: {dist}')

        # If the Dijkastra's Algorithm was successful, dist should contain all the nodes
        if len(dist) == n:
            return max(dist.values())
        else:
            return -1


class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Make graph
        graph = collections.defaultdict(list)
        for time in times:
            source = time[0]
            destination = time[1]
            travel_time = time[2]
            graph[source].append([travel_time, destination])

        # print(f'graph: {graph}')

        signal_received_at = [float('inf')] * (n + 1)

        def bfs(k):

            queue = collections.deque()
            queue.append(k)
            signal_received_at[k] = 0

            while queue:

                curr = queue.popleft()

                if curr not in graph:
                    continue

                for edge in graph[curr]:
                    travel_time = edge[0]
                    neighbor = edge[1]

                    next_time = signal_received_at[curr] + travel_time

                    if next_time < signal_received_at[neighbor]:
                        signal_received_at[neighbor] = next_time
                        queue.append(neighbor)

        # print(f'signal_received_at: {signal_received_at}')

        bfs(k)

        # print(f'signal_received_at: {signal_received_at}')

        ans = float('-inf')
        for i in range(1, n + 1):
            ans = max(ans, signal_received_at[i])

        return ans if ans != float('inf') else -1


class Solution1:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Make adjacency list
        adj = collections.defaultdict(list)
        for time in times:
            source = time[0]
            target = time[1]
            travel_time = time[2]

            adj[source].append([travel_time, target])

        # print(f'adj: {adj}')

        # Sort by ascending travel time
        for source in adj:
            adj[source].sort()

        # print(f'adj: {adj}')

        # + 1 to make it 1-based, and don't use 0th element
        signal_received_at = [float('inf')] * (n + 1)

        def dfs(curr_node, curr_time):
            # No need to update
            if curr_time >= signal_received_at[curr_node]:
                return

            signal_received_at[curr_node] = curr_time

            # ?
            if curr_node not in adj:
                return

            for edge in adj[curr_node]:
                travel_time = edge[0]
                neighbor = edge[1]

                dfs(neighbor, curr_time + travel_time)

        # print(f'signal_received_at: {signal_received_at}')

        dfs(k, 0)

        # print(f'signal_received_at: {signal_received_at}')

        ans = float('-inf')

        for node in range(1, n + 1):
            ans = max(ans, signal_received_at[node])

        return ans if ans != float('inf') else -1


if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    # times = [[2, 3, 2], [2, 1, 1], [3, 4, 1]]
    n = 4
    k = 2
    # 2
    # times = [[1, 2, 1]]
    # n = 2
    # k = 1
    # 1
    # times = [[1, 2, 1]]
    # n = 2
    # k = 2
    # -1
    print(Solution().networkDelayTime(times, n, k))
