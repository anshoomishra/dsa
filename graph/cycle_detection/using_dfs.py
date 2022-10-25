# DFS algo on undirected graph for cycle detection

# Graph build step: Provided edge list

def build_graph(edges,nodes):
    graph = {i:[] for i in range(nodes)}
    for item in edges:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])
    return graph
def print_graph(graph):
    for node in graph:
        print(node,"->",graph[node])


def dfs(graph,src,visited=set()):
    visited.add(src)
    for node in graph[src]:
        if not node in visited:
            dfs(graph,node,visited)
        else:
            return True
    return False
        


if __name__ == "__main__":
    edges = [[0,1],[0,2],[1,2],[1,3],[2,4],[3,5],[4,5]]
    edges = [[0,1],[0,2]]
    print_graph(build_graph(edges,3))
    print(dfs(build_graph(edges,3),0))