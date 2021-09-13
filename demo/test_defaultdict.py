from collections import defaultdict

graph = defaultdict(defaultdict)

graph['a']['b'] = 1
graph['a']['c'] = 2
print(graph)

neighbors = graph['a']
print(neighbors)
for neighbor in neighbors:
    print(neighbor, type(neighbor))

for test in neighbors.items():
    print(test)