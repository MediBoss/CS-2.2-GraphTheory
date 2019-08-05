import heapq
import sys
sys.path.insert(1, '/Users/mediassumani/Documents/dev/cs/Courses/CS-2.2-GraphTheory/challenges')
import graph

# from challenges import Graph
# from challenge_1 import read_file

def depth_first_search(graph, origin, destination, visited=None):
    """DFS to determine if there is a path between two vertices in a weighted directed graph
    """

    if not visited:
        visited = set()

    if origin == destination:
        return True

    visited.add(origin)
    neighbors = origin.get_neighbors()
   
    for neighbor in neighbors:
        if neighbor not in visited:
            if depth_first_search(graph, neighbor, destination, visited):
                return True
                
    return False

def find_shortest_path(graph, source):
    
    # Set the initial distance to the source to 0 and all to infinity
    weight_to_get_to = { node : float('inf') for node in graph }
    weight_to_get_to[source] = 0

    # Keep track of nodes that's already dequeued - which means we've already found the shortest path to them
    visited_nodes = set()

    # Initializing & Creating the priority Queue
    priority_queue = []
    for node in graph:    
        heapq.heappush(priority_queue, (weight_to_get_to[node], node)) # heapq builds an array of tuples with a node and its weight

    while len(priority_queue) > 0:
        # deque the next node from the priority queue
        _, cheapest_node = heapq.heappop(priority_queue)
        # Add the dequeued node in the set of visited nodes
        visited_nodes.add(cheapest_node)

        # Visit the neighbors of the dequeued nodes
        for neighbor, weight in graph[cheapest_node]:

            # Skip the neighbor that's visited already
            if neighbor in visited_nodes:
                continue
            
            # Can we get there cheapely via the neighbor
            if weight_to_get_to[cheapest_node] + weight < weight_to_get_to[neighbor]:
                # Update the cost the cost to reach the node
                weight_to_get_to[neighbor] = weight_to_get_to[cheapest_node] + weight

                # upadte the cost to reach this node in the priority queue
                heapq.heapreplace(priority_queue, (weight_to_get_to[neighbor], neighbor))

    return weight_to_get_to
    
def main():
    
    graph = {}

    graph["A"] = [("B", 10), ("D", 11), ("C", 2)]
    graph["B"] = [("A", 10), ("C", 7)]
    graph["C"] = [("B", 7), ("D", 6), ("A", 2)]
    graph["D"] = [("A", 11), ("C", 6)]

    print(find_shortest_path(graph, "A"))

if __name__ == "__main__":
    main()