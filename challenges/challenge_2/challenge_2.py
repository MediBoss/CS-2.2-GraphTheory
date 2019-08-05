from collections import deque

def breadth_first_search(graph, vertex_key, n):
    """
        Return all nodes that are exactly n connections away from vertex.
    """
    if vertex_key not in graph:
        return

    visited_vertices = set()
    vertex = graph[vertex_key]
    graph_queue = deque([vertex])
    visited_vertices.add(vertex)

    while len(graph_queue) > 0:

        curr_vertex = graph_queue.popleft()
        adj_vertices = curr_vertex.get_neighbors()
        remaining_elements = set(adj_vertices).difference(visited_vertices)
        if len(remaining_elements) > 0:

            for elem in remaining_elements:
                visited_vertices.add(elem)
                graph_queue.append(elem)