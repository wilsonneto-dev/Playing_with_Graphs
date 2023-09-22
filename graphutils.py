def link(g: [], v1: int, v2: int, weight: int):
    g[v1].append((v2, weight))
    g[v2].append((v1, weight))


def graph(number_nodes: int):
    return [[] for _ in range(number_nodes)]
