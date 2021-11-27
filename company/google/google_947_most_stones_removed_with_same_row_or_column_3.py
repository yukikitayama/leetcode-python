"""
- Make a graph
  - dictionary Key: index of a stone, value: list of stones which are connected wit the key stone
    if stone[0] is same of if stone[1] is same
  -
- Find the number of connected components
  - DFS
    - When stack is empty, no more neighbors to visit, so end of one connected component
      - increment num_connected_component
    -
- return length(stones) - number of connected components
"""