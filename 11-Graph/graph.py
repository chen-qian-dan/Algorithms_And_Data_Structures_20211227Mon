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


    def DFS(self, node):
        if not self.dict:
            print("The graph is empty")
        elif not node in self.dict.keys():
            print(f"{node} is not in the graph")
        else:
            stack = list()
            visited = list() 
            stack.append(node)
            while len(stack) > 0:
                tempNode = stack.pop()
                if not tempNode in visited:
                    print(tempNode)
                    visited.append(tempNode)
                    for child in self.dict[tempNode]:
                        stack.append(child)

        

    
def DFS(graph: Graph, node, visitedLst):
    if not graph.dict:
        print("The graph is empty") 
        return 
    if not node in graph.dict.keys():
        print(f"{node} is not in the graph")
        return 

    if node in visitedLst:
        return 

    print(node)
    visitedLst.append(node)
    for child in graph.dict[node]:
        DFS(graph, child, visitedLst)




gDict = {
    "a": ["b", "c"], 
    "b": ["a", "d", "e"],
    "c": ["a", "e"], 
    "d": ["b", "e", "f"], 
    "e": ["d", "f", "c"], 
    "f": ["d", "e"]
}

graph = Graph(gDict)
graph.addEdge("e", "c")
graph.BFS("a")
print("DFS----------------------------")
DFS(graph, "a", [])
print("DFS----------------------------")
graph.DFS("a")
