
#!python
import sys

class Vertex(object):

    def __init__(self, vertex):
        self.id = vertex
        self.neighbors = {}

    def __eq__(self, vertex):
        return self.id == vertex.id

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return self.id

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight
            return True

        return False

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        
        return [neighbor for neighbor,_ in self.neighbors.items()]

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        try:
            return self.neighbors[vertex]
        except KeyError:
            return "Vertex {} not in Graph".format(vertex.id)

class Graph:

    def __init__(self):
        """Initialize a graph object with an empty dictionary, number of edges and vertices"""
        self.graph = {}
        self.edges = 0
        self.vertices = 0

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.graph.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex.
            Time & Space complexity : O(1) | O(1)
        """
        vertex = Vertex(key)
        self.vertices += 1
        self.graph[key] = vertex

        return vertex

    def get_vertex(self, key):
        """Return the vertex if it exists
            Time & Space Complexity : O(1) | O(1)
        """

        vertex = None
        try: 
           vertex = self.graph[key]
        except KeyError:
            raise ValueError("Vertex with key {} not in Graph".format(key))

        return vertex


    def add_edge(self, key1, key2, weight=0):
        """add an edge from vertex with key `key1` to vertex with key `key2` with a cost."""

    
        if key1 not in self.graph and key2 not in self.graph:
            raise ValueError("Both Vertex of keys {} and {} not in Graph".format(key1, key2))
        elif key1 not in self.graph or key2 not in self.graph:
            raise ValueError("Either Vertex of keys {} and {} not in Graph".format(key1, key2))

        elif key1 == key2:
            raise ValueError("Vertex {} can't be its own neighbor".format(key1))
        else:
            # Get the two neighbor verteces
            vertex_one = self.graph[key1]
            vertex_two = self.graph[key2]

            # Code idea from Vicenzo : https://github.com/C3NZ/CS22/blob/master/challenges/graph.py#L77
            added_from = vertex_one.add_neighbor(vertex_two, weight)
            added_to = vertex_two.add_neighbor(vertex_one, weight)

            if added_from and added_to:
                self.edges += 1

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.graph.keys()


def add_many_vertices(vertex_list, graph):

    for vertex in vertex_list:
        graph.add_vertex(vertex)
    
def add_many_edges(edge_list, graph):
    
    for edge in edge_list:

        vertex_one = edge[1]
        vertex_two = edge[3]
        graph.add_edge(vertex_one, vertex_two)
        
     
def read_file(file_name):

    try:
        with open(file_name, "r") as opened_file:

            text = opened_file.read()
            split_text = text.split("\n")
            graph = Graph()

            vertices_list  = split_text[1].split(",")
            edge_list = split_text[2:]

            add_many_vertices(vertices_list, graph)
            add_many_edges(edge_list, graph)        
            
    except IOError:
        raise ValueError("Error : The file {} was not found".format(file_name))

    return (graph, edge_list)


def main():

    text_file = sys.argv[1]
    graph, edge_list = read_file(text_file)
    print("# Vertices: {}\n# Edges: {}\nEdge List:\n{}".format(graph.vertices, graph.edges, edge_list))

if __name__ == "__main__":
    main()