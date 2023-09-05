from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def print_graph(self):
        for node in self.graph:
            print(node,"->",self.graph[node])
    
    def topologicalSortUtil(self, v, visited, stack):
 
        visited[v] = True
 
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        stack.append(v)
 
    def topologicalSort(self):
        visited = [False]*self.vertices
        stack = []
 
        for i in range(self.vertices):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        print(stack[::-1])

if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(3,5)
    graph.add_edge(4,5)
    graph.print_graph()
    graph.topologicalSort()
    
    

