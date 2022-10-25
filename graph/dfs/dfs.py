def build_graph(edges):
    graph = {i:[] for i in range(len(edges))}
    for item in edges:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])
    return graph

def print_graph(graph):
    for node in graph:
        print(node,"->",graph[node])

if __name__ == "__main__":
    # graph = build_graph([[1,0],[1,2],[2,1]])
    print_graph(build_graph([[1,0],[1,2]]))
    