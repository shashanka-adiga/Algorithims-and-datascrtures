from collections import  defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, node, neighbours):
        self.graph[node].append(neighbours)

    def initialize_in_order(self, in_order):
        for node in self.graph:
            in_order[node] = 0
            for neighbours in self.graph[node]:
                in_order[neighbours] = 0

    def topological_sort(self):
        in_order = {}
        self.initialize_in_order(in_order)
        queue = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                in_order[neighbour] += 1
        print(in_order)
        for node in in_order:
            if in_order[node] == 0:
                queue.append(node)
        top_order = []
        count = 0
        while queue:
            node = queue.pop(0)
            top_order.append(node)
            for neighbour in self.graph[node]:
                in_order[neighbour]-=1
                if in_order[neighbour] == 0:
                    queue.append(neighbour)
            count+=1
        if count != self.V:
            print('topological sort not possible')
        else:
            print('topologically sorted array:')
            print(top_order)

g = Graph(6)
g.add_edge(5,4)
g.add_edge(6,4)
g.add_edge(7,4)
g.add_edge(8,4)
g.add_edge(5,8)
g.add_edge(8,9)
g.add_edge(7,9)
g.topological_sort()

