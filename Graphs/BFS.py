from  collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u , v):
        self.graph[u].append(v)

    def bfs(self, root):
        visited = []
        queue = [root]
        visited.append(root)
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for neighbors in self.graph[node]:
                if neighbors not in visited:
                    queue.append(neighbors)
                    visited.append(neighbors)


g = Graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(4,6)
g.add_edge(5,6)
g.bfs(1)

