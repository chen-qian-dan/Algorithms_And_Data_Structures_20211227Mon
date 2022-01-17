# Single Source Shortest Path Problem

from collections import defaultdict 
from copy import deepcopy

class Graph:
    def __init__(self, gdict = None):
        self.dict = defaultdict()
        if gdict:
            self.dict = defaultdict(int, gdict)

    def addEdge(self, node1, node2):
        if not node1 in self.dict.keys(): 
            self.dict[node1] = list()
        
        if not node2 in self.dict[node1]:
            self.dict[node1].append(node2)


    def BFSforSSSPP(self, startNode, endNode):
        if not startNode in self.dict.keys() and endNode not in self.dict.keys():
            return ("Either the start node or end node is not in the graph")
        elif startNode == endNode:
            return [startNode]
        else:
            visited = list()
            q = list()
            parents = defaultdict()
            q.append(startNode)
            parents[startNode] = None 
            while len(q) > 0:
                node = q.pop(0)
                if node not in visited:
                    visited.append(node)
                    if node not in self.dict.keys():
                        self.dict[node] = list()
                    for child in self.dict[node]:
                        if child not in visited:
                            q.append(child)
                            parents[child] = node

        path = list()
        node = endNode 
        path.insert(0, node)
        while parents[node]:
            path.insert(0, parents[node])
            node = parents[node]
            if node == endNode:
                break 
        return path 

    
    def BFSforSSSPPVideo(self, startNode, endNode): # time O(E), space O(E)
        q = list()
        q.append([startNode])
        while len(q) > 0: # ----- time O(V)
            path = q.pop(0)
            if path[-1] == endNode:
                return path 
            else:
                node = path[-1]
                if node not in self.dict.keys():
                    self.dict[node] = list()
                for child in self.dict[node]: # ----- time O(E)
                    newpath = list(path)
                    newpath.append(child)
                    q.append(newpath)

        return path 

    



graph = Graph()
graph.addEdge("A", "C")
graph.addEdge("C", "E")
graph.addEdge("E", "H")
graph.addEdge("E", "F")
graph.addEdge("F", "G")
graph.addEdge("B", "D")
graph.addEdge("B", "C")
graph.addEdge("D", "F")

print(graph.BFSforSSSPP("A", "G"))
print(graph.BFSforSSSPPVideo("A", "G"))

        