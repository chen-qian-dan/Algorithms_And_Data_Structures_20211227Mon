class Graph:
    def __init__(self, gdict = None): # by ref 
        if gdict is None:
            gdict = dict()
        self.gdict = gdict 


    def addEdge(self, vertex, edge):
        if not vertex in self.gdict.keys():
            self.gdict[vertex] = set()
        self.gdict[vertex].add(edge)


g = {"a": ("b", "c"), 
    "b": ("a", "d", "e"), 
    "c": ("a", "e"), 
    "d": ("b", "e", "f"), 
    "e": ("d", "f"), 
    "f": ("d", "e")
    }

graph = Graph(gdict = g)
print(graph.gdict)