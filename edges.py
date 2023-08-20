def convert_to_edges(G):

    n = len(G)
    visited = [False for _ in range(n)]
    E = []
    for i in range(n):
        visited[i] = True
        for edge in G[i]:
            if not visited[edge[0]]:
                E.append((edge[1], i, edge[0]))

    E.sort(key = lambda x:x[0])
    #E: (waga, u, v)
    return E
