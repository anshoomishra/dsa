def build_graph(arr):
    graph = {i:[] for i in range(len(arr))}
    for i in range(len(arr)):
        if arr[i] not in graph[i]:
            graph[i].append(arr[i])
        
    print(graph)


arr = [1,2,1,3,1,2,3,4,1]
build_graph(arr)