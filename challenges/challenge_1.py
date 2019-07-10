class Graph(object):
    
    def __init__(self, type, vertices, edges, weighted=False):
        
        self.type = type
        self.vertices = vertices
        self.edges = edges

    def __str__(self):

        return "Graph of type {} with vertices {} and edges {}".format(self.type, self.vertices, self.edges)
    def num_of_vertices(self):
        pass

    def num_of_edges(self):
        pass

    def edges_with_weights(self):
        pass


def read_file(file_name):

    with open(file_name, "r") as opened_file:
        
        text = opened_file.read()
        split_text = text.split("\n")
        
        g = Graph(split_text[0], split_text[1].split(","), split_text[2:])
        print(g)


def main():
    
    read_file("test.txt")

if __name__ == "__main__":
    main()