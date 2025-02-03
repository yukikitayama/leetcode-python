from typing import List
import collections


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:

        def bfs(start_node, visited_nodes, revered_graph):
            # [(node, distance), ...]
            queue = collections.deque([(start_node, 0)])
            max_distance = 0
            while queue:
                current_node, current_distance = queue.popleft()
                for neighbor in reversed_graph[current_node]:
                    if neighbor in visited_nodes:
                        continue
                    visited_nodes.add(neighbor)
                    queue.append((neighbor, current_distance + 1))
                    max_distance = max(max_distance, current_distance + 1)
            return max_distance

        reversed_graph = collections.defaultdict(list)
        for i in range(len(favorite)):
            reversed_graph[favorite[i]].append(i)

        longest_cycle = 0
        two_cycle_invitations = 0
        visited = [False] * len(favorite)
        for person in range(len(favorite)):
            if not visited[person]:

                visited_person_to_distance = dict()
                current_person = person
                distance = 0
                while True:

                    if visited[current_person]:
                        break

                    visited[current_person] = True
                    visited_person_to_distance[current_person] = distance
                    distance += 1
                    next_person = favorite[current_person]

                    # Detect cycle
                    if next_person in visited_person_to_distance:
                        cycle_length = distance - visited_person_to_distance[next_person]
                        longest_cycle = max(longest_cycle, cycle_length)

                        if cycle_length == 2:
                            visited_nodes = set([current_person, next_person])
                            two_cycle_invitations += (
                                    2
                                    + bfs(next_person, visited_nodes, reversed_graph)
                                    + bfs(current_person, visited_nodes, reversed_graph)
                            )

                        break

                    current_person = next_person

        return max(longest_cycle, two_cycle_invitations)