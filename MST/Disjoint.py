class DisjointSet:
    def __init__(self,vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices,0)
    
    def find(self,item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[x] = y
            
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[y] = x
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
if __name__=="main":
    vertices = ["A","B","C","D","E"]

    ds = DisjointSet(vertices)

    ds.union("A","B")
    ds.union("C","D")

    print(ds.find("B"))