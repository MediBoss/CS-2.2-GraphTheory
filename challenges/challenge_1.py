import sys

class Graph(object):
    
    def __init__(self, type, vertices, edges, weighted=False):
        
        self.type = type
        self.vertices = vertices
        self.edges = edges

    def __str__(self):

        return "Graph of type {} with vertices {} and edges {}".format(self.type, self.vertices, self.edges)
    def num_of_vertices(self):
        return len(self.vertices)

    def num_of_edges(self):
        return len(self.edges)

    def edges_with_weights(self):
        return self.edges


def read_file(file_name):

    with open(file_name, "r") as opened_file:
        
        text = opened_file.read()
        split_text = text.split("\n")
        
        graph = Graph(split_text[0], split_text[1].split(","), split_text[2:])

    return graph


def main():
    
    graph = read_file("test.txt")


if __name__ == "__main__":
    main()