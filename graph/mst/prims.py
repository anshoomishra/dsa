# MST-PRIM (G, w, r) {
#     for each key ∈ G.V
#         u.key = ∞
#         u.parent = NIL
#     r.key = 0
#     Q = G.V

#     while (Q ≠ ø)
#         u = Extract-Min(Q)
#         for each v ∈ G.Adj[u]
#             if (v ∈ Q)
#                 alt = w(u,v)    <== relax function, Pay attention here
#                 if alt < v.key
#                     v.parent = u
#                     v.key = alt
# }

def build_graph(edges):
    graph = {i:[] for i in range(len(edges))}
    for edge in edges:
        graph[edge[0]].append([edge[1],edge[2]])
        graph[edge[1]].append([edge[0],edge[2]])
    return graph

def prims_algo(graph,src):
    
    pass

def print_graph(graph):
    for node in graph:
        print(node,"->",graph[node])



if __name__ == "__main__":
    edges = [
        [0,1,1],
        [0,2,2],
        [1,3,1],
        [1,2,3],
        [2,4,4],
        [2,3,2],
    ]
    graph = build_graph(edges)
    print(graph)