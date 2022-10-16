from collections import defaultdict
from typing import List

class Graph:
    def __init__(self,node_list:List) -> None:
        self.node_list = node_list
        self.adj_list = defaultdict(list)

        for edge in self.node_list:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])
    
    def printgraph(self):
        for node in self.adj_list:
            print(node, "->",self.adj_list[node])

            
    def insert_edge(self,edge):

        self.adj_list[edge[0]].append(edge[1])
        self.adj_list[edge[1]].append(edge[0])




if __name__ == "__main__":
    array_list = [[0,1],[1,2],[2,3],[2,0]]
    graph = Graph(array_list)
    graph.printgraph()
    graph.insert_edge([2,4])
    graph.insert_edge([2,4])
    print("**** New Graph ******")
    graph.printgraph()
