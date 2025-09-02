import heapq

# heap functions

minheap = []
heapq.heappush(minheap, 1)
heapq.heappush(minheap, 5)
heapq.heappush(minheap, 79)
heapq.heappush(minheap, 2)

print(minheap)


x = heapq.heappop(minheap)
print(x)  # 1
print(minheap)  # [2, 5, 79]


maxheap = []
heapq.heappush(maxheap, -1)
heapq.heappush(maxheap, -5)
heapq.heappush(maxheap, -79)
heapq.heappush(maxheap, -2)

heapq.heappop(maxheap)

print(maxheap) # [-5, -2, -79]
y = -heapq.heappop(maxheap)
print(y)  # 79
print(maxheap)  # [-5, -2]


heaplist = [5, 3, 8, 1, 2, 7]
heapq.heapify(heaplist)
print(heaplist)  # [1, 2, 7, 3, 5, 8] heapified list