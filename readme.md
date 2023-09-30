# Let`s play Grahs

I`m studying and having fun with some base graph concepts and the main algorithms

### Dijkstra Algorithm

Dijkstra's algorithm is a graph search algorithm that solves the single-source shortest path problem for a graph with non-negative edge path costs, producing a shortest path tree. Given a graph and a source vertex, the algorithm finds the shortest path from the source to all other vertices. It works by iteratively selecting the vertex with the smallest known distance from the source and exploring its neighbors, updating their shortest path distances if a shorter path is found.

In essence: Start at the source, explore neighbors, always choose the next closest vertex, and repeat until all vertices are visited.

```python
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
```

### Bellman-Ford Algorithm

The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted graph. It is slower than Dijkstra's algorithm for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

Also, Bellman-Ford is used in detecting negative cycles in a graph.

```python
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
```


### References

- [What is Dijkstra Algorithm - Geeks for Geeks](https://www.geeksforgeeks.org/introduction-to-dijkstras-shortest-path-algorithm/)
- [Dijkstra Algorithm - Abdu Bari](https://www.youtube.com/watch?v=XB4MIexjvY0)
- [Dijkstra Algorithm - NeetCodeIO](https://www.youtube.com/watch?v=XEb7_z5dG3c)