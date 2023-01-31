class Graph:
    def __init__(self,gdict=None):
        if not gdict:
            gdict = {}
        self.gdict = gdict
    
    def addedge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        visited = [vertex]
        queue = []
        queue.append(vertex)
        while len(queue) !=0:
            devertex = queue.pop(0)
            print(devertex)
            for adjacentvertex in self.gdict[devertex]:
                if adjacentvertex not in visited:
                    queue.append(adjacentvertex)
                    visited.append(adjacentvertex)
    
    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while len(stack)!=0:
            popvertex = stack.pop()
            print(popvertex)
            for adjacentvertex in self.gdict[popvertex]:
                if adjacentvertex not in visited:
                    stack.append(adjacentvertex)
                    visited.append(adjacentvertex)



# graph_elements = { 
#    "a" : ["b","c"],
#    "b" : ["a", "d"],
#    "c" : ["a", "d"],
#    "d" : ["e"],
#    "e" : ["d"]
# }

customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
            }
graph = Graph(customDict)
# graph.bfs("a")
graph.dfs("a")