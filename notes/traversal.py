
def dfs(graph, start, visited=None):
    
    if not visited:
        visited = set()
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
        continue

    return visited

def find_path(graph, origin, destination, visited=None):
    
    if not visited:
        visited = set()
    
    visited.add(origin)

    # Base case
    if origin == destination:
        return True

    for neighbor in graph[origin]:
        if neighbor not in visited:
            # Recursive case
            print(neighbor)
            find_path(graph, neighbor, destination, visited)


    return False

def bfs(graph):
    pass

def main():
    
    graph = {}
    graph["A"] = ["E", "B"]
    graph["E"] = ["A", "C"]
    graph["C"] = ["E", "F"]
    graph["F"] = ["C", "D"]
    graph["D"] = ["F", "B"]
    graph["B"] = ["D", "A"]

    dfs(graph, "A")
    # origin = "A"
    # destination = "F"
    # #print("Is there path from {} to {} : ".format(origin, destination), find_path(graph, origin, destination))
    # find_path(graph, origin, destination)
if __name__ == "__main__":
    main()