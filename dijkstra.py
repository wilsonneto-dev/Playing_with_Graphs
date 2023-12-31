import heapq
from graphutils import graph, link

graph1 = graph(7)
link(graph1, 0, 1, 2)
link(graph1, 0, 2, 6)
link(graph1, 1, 3, 5)
link(graph1, 2, 3, 8)
link(graph1, 3, 5, 15)
link(graph1, 3, 4, 10)
link(graph1, 4, 5, 6)
link(graph1, 5, 6, 6)
link(graph1, 4, 6, 2)


def dijkstra_min_distance(g: [[(int, int)]], start: int, destination: int):
    distances = [float('inf')] * len(g)
    distances[start] = 0
    min_heap = [(0, start)]  # min heap / priority queue

    while min_heap:
        distance, curr = heapq.heappop(min_heap)
        if distance < distances[curr]:
            continue

        for edge_neighbor, edge_distance in g[curr]:
            new_distance = distances[curr] + edge_distance
            if new_distance < distances[edge_neighbor]:
                distances[edge_neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, edge_neighbor))

    return distances[destination]


test_cases = [
    {"inputs": [graph1, 0, 6], "expected": 19},
    {"inputs": [graph1, 0, 2], "expected": 6},
    {"inputs": [graph1, 0, 5], "expected": 22}
]

for test_case in test_cases:
    result = (dijkstra_min_distance(*test_case["inputs"]))
    assert result == test_case["expected"], f"Dijkstra {test_case}: result {result}"
    print(f"✅ Test OK: {test_case}")
