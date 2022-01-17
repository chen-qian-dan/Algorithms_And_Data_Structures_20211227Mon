# Topological Sort

class Graph:
    def __init__(self, gdict = None):
        if not gdict:
            self.dict = dict()
        else:
            self.dict = gdict

    def addEdge(self, node1, node2):
        if not node1 in self.dict.keys():
            self.dict[node1] = list()

        if not node2 in self.dict[node1]:
            self.dict[node1].append(node2)


    
    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        if not v in self.dict.keys():
            self.dict[v] = list()

        for i in self.dict[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)


    def topologicalSort(self):
        visited = list()
        stack = list()
        for k in list(self.dict):
            if not k in visited:
                self.topologicalSortUtil(k, visited, stack)
        print(stack)



graph = Graph()
graph.addEdge("A", "C")
graph.addEdge("C", "E")
graph.addEdge("E", "H")
graph.addEdge("E", "F")
graph.addEdge("F", "G")
graph.addEdge("B", "D")
graph.addEdge("B", "C")
graph.addEdge("D", "F")

graph.topologicalSort()
