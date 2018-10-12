graph={
    "a":["c"],
    "b":["c","e"],
    "c":["a","b","d","e"],
    "d":["c"],
    "e":["c","b"],
    "f":[]
}

def get_node(graph):
    edege=[]
    for node in graph:
        for neighbour in graph[node]:
            edege.append((node,neighbour))
    return edege

print(get_node(graph))
