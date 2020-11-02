# Bfs or printing nodes of tree level wise
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def dfs_util(self,node,visited):
        if node not in visited:
            visited.append(node)
        for i in self.graph[node]:
            if i not in visited:
                visited.append(i)

    def dfs(self,V):
        visited = []
        for i in self.graph:
            self.dfs_util(i,visited)
        print(visited)
g = Graph()
g.add_edge(0,3)
g.add_edge(0,4)
g.add_edge(4,7)
g.add_edge(3,9)
g.add_edge(9,1)
g.dfs(0)

# dfs for connected graph
# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
#
#     def addEdge(self,u,v):
#         self.graph[u].append(v)
#
#     def dfsUtil(self,u,visited):
#         if u not in visited:
#             visited.append(u)
#         if u in self.graph:
#             for i in self.graph[u]:
#                 if i not in visited:
#                     self.dfsUtil(i,visited)
#
#     def dfs(self,s,V):
#         visited = []
#         for s in self.graph:
#             self.dfsUtil(s,visited)
#         print(visited)
#
# g = Graph()
# g.addEdge(0,1)
# g.addEdge(0,2)
# g.addEdge(1,3)
# g.addEdge(2,4)
# g.addEdge(5,4)
# g.dfs(0,5)

#   0
# 34
# 79
# 1