def bridges(G):

    # G - adj. list

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    children = [[] for _ in range(n)]
    low = [None for _ in range(n)]
    time = 0
    B = []

    parent[0] = 0

    def DFSVisit(node):

        nonlocal time
        #print("odwiedzam node:", node, "time =", time)


        d[node] = time
        low[node] = time

        time += 1
        visited[node] = True

        for neighbour in G[node]:

            if visited[neighbour] and parent[node] != neighbour:

                #print("sprawdzam krawdz wsteczna", node, neighbour)
                low[node] = min(low[node], d[neighbour])
                #print("low node", node, "to", low[node])

        for neighbour in G[node]:

            if not visited[neighbour]:
                parent[neighbour] = node
                children[node].append(neighbour)
                DFSVisit(neighbour)
                low[node] = min(low[node], low[neighbour])
                #print("wracam z", neighbour, "low node", node, "to", low[node])

        if node != 0:
            low[parent[node]] = min(low[parent[node]], low[node])

        if d[node] == low[node] and node != 0:

            x = min(node, parent[node])
            y = max(node, parent[node])
            B.append((x, y))


    for node in range(n):

        if not visited[node]:
            DFSVisit(node)

    articulation_points = []

    if len(children[0]) > 1:
        articulation_points.append(0)

    for node in range(1, n):

        for child in children[node]:

            if low[child] >= d[node]:

                articulation_points.append(node)
                break

    #return low
    #return articulation_points
    return B
