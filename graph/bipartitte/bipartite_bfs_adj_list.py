def build_graph(edges):
    graph = {i:[] for i in range(len(edges))}
    for edge in edges :
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def is_partite(graph,src):
    queue = [(src,0)]
    visited_color = [-1]*6
    visited_color[src] = 0
    while queue:
        node,color = queue.pop(0)
        for adj in graph[node]:
            if visited_color[adj] == color:
                return False
            if visited_color[adj] == -1:
                if color == 0:
                    visited_color[adj] = 1
                    
                else:
                    visited_color[adj] = 0
                queue.append((adj,visited_color[adj]))
                    
    return True



if __name__ == "__main__":
    edges = [[0,1],[1,3],[0,2],[2,4],[3,5],[4,5]]
    graph = build_graph(edges)
    print(graph)
    print(is_partite(graph,0))
