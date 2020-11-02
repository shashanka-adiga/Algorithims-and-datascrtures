from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


    def all_paths(self, src , dest, path, visited):
        visited.append(src)
        path.append(src)
        if src == dest:
            print(path)
        else:
            for i in self.graph[src]:
                if i not in visited:
                    self.all_paths(i, dest, path, visited)
        path.pop()
        visited.pop()

    # solution = 0
    # def all_paths(self, src, dest, path, len_path):
    #     visited = []
    #     if src not in visited:
    #         visited.append(src)
    #     if len(path) <= len_path:
    #         path.append(src)
    #     else:
    #         path[len_path] = src
    #     len_path+=1
    #     if src == dest:
    #         self.solution+=1
    #         print("solution no", self.solution)
    #         for i in path:
    #             if i == dest:
    #                 break
    #             else:
    #                 print(i)
    #     for node in self.graph[src]:
    #         if node not in visited:
    #             self.all_paths(node, dest, path, len_path)


g = Graph()
g.add_edge(1,3)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(1,60)
g.add_edge(60,4)
path = []
visited = []
g.all_paths(1,4,path, visited)