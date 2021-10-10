import heapq

item_1 = (0, 1)
item_2 = (1, 3)
item_3 = (1, 2)

h = []

heapq.heappush(h, item_1)
heapq.heappush(h, item_2)
heapq.heappush(h, item_3)

print(h)

print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
