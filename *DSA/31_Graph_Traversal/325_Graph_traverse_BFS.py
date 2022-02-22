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


    def BFS(self, vertex): # time O(v + e) space O(v + e)
        if self.gdict is None:
            return "The graph does not exist"

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


    def DFS(self, vertex): # time O(v + e)  space O(v + e)
        if self.gdict is None:
            return "The graph does not exist"
        if vertex not in self.gdict.keys():
            return False 
        ret = list()
        visitedDict = Dict.fromkeys(self.gdict.keys(), False)
        stack = deque()
        stack.append(vertex)
        while len(stack):
            node = stack.pop()
            if visitedDict[node] is False:
                ret.append(node)
                visitedDict[node] = True 
                for v in self.gdict[node]:
                    if visitedDict[v] is False:
                        stack.append(v)
                    
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
print(graph.DFS("a"))