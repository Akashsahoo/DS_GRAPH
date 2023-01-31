class Graph:
    def __init__(self,gdict=None) :
        if not gdict:
            self.gdict = {}
            
        else:
           self.gdict = gdict
        self.distancedict = {}
        self.visiteddict = {}
        self.infinite = 1e7
        self.path = {}

    def addvertex(self,vertex):
        self.gdict[vertex] = []
        self.distancedict[vertex] = self.infinite
        self.visiteddict[vertex] = False
        self.path[vertex] = None

    def addedge(self,fromvertex,tovertex,weight):
        if not fromvertex in self.gdict:
            self.addvertex(fromvertex)
        # self.gdict[fromvertex].append((tovertex,weight))
        self.gdict[fromvertex].append({tovertex:weight})
        # tuple = (tovertex,"weight")
        # self.gdict[fromvertex].append((tovertex:tovertex,"weight":weight))
        if not tovertex in self.gdict:
            self.addvertex(tovertex)
        # self.gdict[tovertex].append((fromvertex,weight)
        self.gdict[tovertex].append({fromvertex:weight})
        # self.gdict[tovertex].append({fromvertex:fromvertex,"weight":weight})
    
    def minimumvertex(self):
        min = self.infinite
        for vertex in self.distancedict:
            if self.distancedict[vertex] < min and self.visiteddict[vertex] == False:
                min = self.distancedict[vertex]
                min_vertex = vertex
        return min_vertex
    def dijkstra(self,source):
        self.distancedict[source] = 0
        for key in self.path:
            self.path[key] = str(source)
        for _ in range(len(self.gdict)):
            min_vertex = self.minimumvertex()
            self.visiteddict[min_vertex] = True
            for adjacentvetexdict in self.gdict[min_vertex]:
               
                for adjancentvertexkey in adjacentvetexdict.keys():
                   
                    if not self.visiteddict[adjancentvertexkey] and int(self.distancedict[adjancentvertexkey]) > int(self.distancedict[min_vertex]) + adjacentvetexdict[adjancentvertexkey] :
                      self.distancedict[adjancentvertexkey] = self.distancedict[min_vertex] + int(adjacentvetexdict[adjancentvertexkey] )
                      if self.path[adjancentvertexkey] != min_vertex:
                         self.path[adjancentvertexkey] = str(self.path[adjancentvertexkey]+str(min_vertex))
                      
                
                    
    def distancematrix(self):
        print(self.distancedict)
        print(self.path)

graph = Graph()

graph.addedge("A","B",4)
graph.addedge("A","H",8)

graph.addedge("B","C",8)
graph.addedge("B","H",11)

graph.addedge("C","D",7)
graph.addedge("C","F",4)
graph.addedge("C","I",2)


graph.addedge("D","E",9)
graph.addedge("D","F",14)

graph.addedge("E","F",10)

graph.addedge("F","G",2)

graph.addedge("G","H",1)
graph.addedge("G","I",6)

graph.addedge("H","I",7)
# print(graph.gdict)
graph.dijkstra('A')

graph.distancematrix()



#            #A  B  C  D  E  F  G  H   I  
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],# A
# 		   [4, 0, 8, 0, 0, 0, 0, 11, 0],# B
# 		   [0, 8, 0, 7, 0, 4, 0, 0, 2], # C
# 		   [0, 0, 7, 0, 9, 14, 0, 0, 0], # D
# 		   [0, 0, 0, 9, 0, 10, 0, 0, 0], # E
# 		   [0, 0, 4, 14, 10, 0, 2, 0, 0], # F
# 		   [0, 0, 0, 0, 0, 2, 0, 1, 6], # G
# 		   [8, 11, 0, 0, 0, 0, 1, 0, 7], # H
# 		    [0, 0, 2, 0, 0, 0, 6, 7, 0]] # I

# g.dijkstra(0)