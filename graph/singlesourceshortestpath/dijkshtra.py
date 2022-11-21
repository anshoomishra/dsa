# Dijkstra (G, w, r) {
#     for each key ∈ G.V
#         u.key = ∞
#         u.parent = NIL
#     r.key = 0
#     Q = G.V

#     while (Q ≠ ø)
#         u = Extract-Min(Q)
#         for each v ∈ G.Adj[u]
#             if (v ∈ Q)
#                 alt = w(u,v) + u.key  <== relax function, Pay attention here
#                 if alt < v.key
#                     v.parent = u
#                     v.key = alt
# }