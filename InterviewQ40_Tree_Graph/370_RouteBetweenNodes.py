"""
370 - Route between nodes

Given a directed graph and two nodes (S and E), design an algorithm to find out whether 
there is a route from S to E. 

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        # TODO

"""

"""
1. Problem 
Note: there maybe circle, so need to mark if the node is visited. 
2. Input: nodeS, nodeE
3. Output: bool
4. Edge cases:
if S or E are not in the graph
5. Time complexity
6. Space complexity
"""



# Wrong 

# class Graph:
#     def __init__(self, gdict = None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict
    
#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)
    
#     def checkRoute(self, startNode, endNode) -> bool:
#         if startNode not in self.gdict.keys() or endNode not in self.gdict.keys():
#             return False 

#         if startNode == endNode:
#             return True 

#         for child in self.gdict[startNode]:
#             if self.checkRoute(child, endNode):
#                 return True 
#         return False 



customDict = {"a": ["c", "d", "b"], 
            "b": ["j"], 
            "c": ["g"], 
            "d": [], 
            "e": ["f", "a"], 
            "f": ["i"], 
            "g": ["d", "h"], 
            "h": [], 
            "i": [], 
            "j": []
            }



class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        """
        - Create func with startNode and endNode
        - Create queue and enqueue startNode to it
        - Find all the neighbors of the just enqueued node and enqueue them into the queue
        - Repeat this process until the end of the elements in graph
        - if during the above process at some point in time we encounter the destination node, we return True. 
        - Mark visited nodes as visited
        """
        q = list()
        q.append(startNode)
        visitd = list()
        
        while len(q) > 0:
            node = q.pop(0)
            visitd.append(node)
            if node == endNode:
                return True 
            for child in self.gdict[node]:
                if child not in visitd:
                    q.append(child)
        return False 

graph = Graph(customDict)
print(graph.checkRoute("a", "e")) # expect Fales 
print(graph.checkRoute("e", "a")) # expect True 
print(graph.checkRoute("a", "j")) # expect True 
   





        
