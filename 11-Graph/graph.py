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


    def BFS(self, node):
        if not self.dict:
            print("The graph is empty") 
        if not node in self.dict.keys():
            print(f"{node} is not in the graph")
            return 

        visited = list()
        q = list()
        q.append(node)
        while len(q) > 0:
            tempNode = q.pop(0)
            if not tempNode in visited:
                visited.append(tempNode)
                print(tempNode)
                for child in self.dict[tempNode]:
                    q.append(child)


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
graph.BFS("a")