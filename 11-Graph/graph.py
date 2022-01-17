# Graph

# create
class Graph:
    def __init__(self, gDict = None):
        if not gDict:
            self.dict = dict()
        else:
            self.dict = gDict


    def addEdge(self, node1, node2):
        if not node1 in self.dict.keys():
            self.dict[node1] = list()

        self.dict[node1].append(node2)



gDict = {
    "a": ["b", "c"], 
    "b": ["a", "d", "e"],
    "c": ["a", "e"], 
    "d": ["b", "e", "f"], 
    "e": ["d", "f"], 
    "f": ["d", "e"]
}

graph = Graph(gDict)
graph.addEdge("e", "c")