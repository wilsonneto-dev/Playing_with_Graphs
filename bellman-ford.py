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

graph_neg = graph(7)
link(graph1, 0, 1, 2)
link(graph1, 0, 2, 6)
link(graph1, 1, 3, 5)
link(graph1, 2, 3, 8)
link(graph1, 3, 5, 15)
link(graph1, 3, 4, 10)
link(graph1, 4, 5, 6)
link(graph1, 5, 6, 6)
link(graph1, 4, 6, 2)


def bellman_ford(g: [[(int, int)]], start: int, destination: int):
    distances = [float('inf')] * len(g)
    distances[start] = 0

    # getting the distances
    for _ in range(len(g) - 1):
        # relaxing the edges
        for curr in range(len(g)):
            for dest, cost in g[curr]:
                new_distance = distances[curr] + cost
                if distances[dest] > new_distance:
                    distances[dest] = new_distance

    # checking for negative cycles
    # relax the edges one more time, if a modification happens, we have a negative cycle
    for curr in range(len(g)):
        for dest, cost in g[curr]:
            new_distance = distances[curr] + cost
            if distances[dest] > new_distance:
                raise ValueError("Graph with negative cycle :/")

    return distances[destination]


test_cases = [
    {"inputs": [graph1, 0, 6], "expected": 19},
    {"inputs": [graph1, 0, 2], "expected": 6},
    {"inputs": [graph1, 0, 5], "expected": 22}
]

negative_cycle_test_cases = [
    {"inputs": [graph1, 0, 6], "expected": 19},
    {"inputs": [graph1, 0, 2], "expected": 6},
    {"inputs": [graph1, 0, 5], "expected": 22}
]

for test_case in test_cases:
    result = (bellman_ford(*test_case["inputs"]))
    assert result == test_case["expected"], f"Bellman Ford {test_case}: result {result}"
    print(f"✅ Test OK: {test_case}")
