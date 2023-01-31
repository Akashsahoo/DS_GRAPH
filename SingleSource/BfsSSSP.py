#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        visited = [start]
        while queue:
            print(queue)
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                if adjacent not in visited:
                    visited.append(adjacent)
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)
                

# customDict = { "a" : ["b", "c"],
#                "b" : ["d", "g"],
#                "c" : ["d", "e"],
#                "d" : ["f"],
#                "e" : ["f"],
#                "g" : ["f"]
#             }

customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
            }
g = Graph(customDict)
print(g.bfs("a", "f"))
