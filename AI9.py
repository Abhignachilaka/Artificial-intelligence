import sys
def nearest_neighbor(graph, start_node):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    path = [start_node]
    visited[start_node] = True
    for _ in range(num_nodes - 1):
        current_node = path[-1]
        nearest_neighbor = None
        min_distance = sys.maxsize
        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[current_node][neighbor] < min_distance:
                nearest_neighbor = neighbor
                min_distance = graph[current_node][neighbor]
        path.append(nearest_neighbor)
        visited[nearest_neighbor] = True
    path.append(path[0])
    return path
graph = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
start_node = 0
tour = nearest_neighbor(graph, start_node)
print("Approximate TSP Tour:", tour)
