
def dfs_recursive(graph, start, visited=None):
    
    if not visited:
        visited = set()

    visited.add(start)

    for neighbor in graph[start]:

        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

        continue
    
    return visited

def main():
    
    graph = {}
    graph["A"] = ["E", "B"]
    graph["E"] = ["A", "C"]
    graph["C"] = ["E", "F"]
    graph["F"] = ["C", "D"]
    graph["D"] = ["F", "B"]
    graph["B"] = ["D", "A"]

    print(dfs_recursive(graph, "E"))

if __name__ == "__main__":
    main()