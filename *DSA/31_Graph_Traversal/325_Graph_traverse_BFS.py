from typing import Dict 
from collections import deque 

class Graph:
    def __init__(self, gdict = None): # by ref 
        if gdict is None:
            gdict = dict()
        self.gdict = gdict 


    def addEdge(self, vertex, edge):
        if not vertex in self.gdict.keys():
            self.gdict[vertex] = set()
        self.gdict[vertex].add(edge)


    def BFS(self, vertex):
        if self.gdict is None:
            return "The graph is empty"

        visitedDict = Dict.fromkeys(self.gdict.keys(), False)
        q = deque()
        q.append(vertex)
        ret = list()
        while len(q) > 0:
            node = q.popleft()
            ret.append(node)
            visitedDict[node] = True 
            for v in self.gdict[node]:
                if visitedDict[v] is False:
                    visitedDict[v] = True 
                    q.append(v)

        return ret 


g = {"a": ("b", "c"), 
    "b": ("a", "d", "e"), 
    "c": ("a", "e"), 
    "d": ("b", "e", "f"), 
    "e": ("d", "f"), 
    "f": ("d", "e")
    }

graph = Graph(gdict = g)
print(graph.gdict)
print(graph.BFS("a"))