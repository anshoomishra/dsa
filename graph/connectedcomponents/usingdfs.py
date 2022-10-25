from collections import defaultdict
class Graph:
    def __init__(self,edges) -> None:
        self.adj_list = defaultdict(list)

        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])
    
def printgraph(graph):
    for node in graph.adj_list:
        print(node,"->",graph.adj_list[node])
visited=set()
def dfs_utils(graph,src):
    visited.add(src)
    for node in graph[src]:
        if not node in visited:
            dfs_utils(graph,node)
        

def dfs(graph):
    count = 0
    for node in graph:
        if not node in visited:
            count+=1
            dfs_utils(graph,node)

    return count

if __name__ == "__main__":
    graph = Graph([[0,1],[2,3],[4,5]])
    printgraph(graph)
    print(dfs(graph.adj_list))