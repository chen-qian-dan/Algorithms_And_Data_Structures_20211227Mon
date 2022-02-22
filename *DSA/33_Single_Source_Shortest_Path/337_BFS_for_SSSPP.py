
from collections import deque 
from typing import Dict 

class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            self.gdict = {}
        self.gdict = gdict 

    def bfs(self, start, end): # time: O(E) space O(E)
        """
        why is not O(E+V), because in BFS, it is O(E+V)
        because in the normal BFS, we need to visit all E, including the isolated node
        but, here, no need to visit isolated node
        """
        # if start not in self.gdict.keys() or end not in self.gdict.keys():
        #     return []
        visitedDict = Dict.fromkeys(self.gdict.keys(), False)
        q = deque()
        q.append([start])
        visitedDict[start] = True
        while len(q) > 0: # O(V)
            path = q.popleft()
            node = path[-1]
            if node == end:
                return path
            for n in self.gdict[node]: # O(E)
                if visitedDict[n] is False:
                    visitedDict[n] = True
                    newPath = path[:]
                    newPath.append(n)
                    q.append(newPath)


gdict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"],
    "f": []
}

g = Graph(gdict)
print(g.bfs("a", "f")) # expect [a, b, d, f]



        
