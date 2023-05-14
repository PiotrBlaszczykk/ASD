def bridges(G):

    # G - adj. list

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    low = [None for _ in range(n)]
    time = 0
    B = []


    def DFSVisit(node):

        nonlocal time

        d[node] = time
        low[node] = time

        time += 1
        visited[node] = True

        for neighbour in G[node]:

            if not visited[neighbour]:
                parent[neighbour] = node
                DFSVisit(neighbour)
            elif parent[node] != neighbour:
                low[node] = min(d[node], d[neighbour])

        if node != 0:
            low[parent[node]] = min(low[parent[node]], low[node])

        if d[node] == low[node] and node != 0:

            x = min(node, parent[node])
            y = max(node, parent[node])
            B.append((x, y))


    for node in range(n):

        if not visited[node]:
            DFSVisit(node)

    # print(low)

    points = [0 for _ in range(n)]
    breaking_points = []

    for bridge in B:

        u = bridge[0]
        v = bridge[1]

        points[u] += 1
        points[v] += 1

    for i in range(n):

        if points[i] != 0:

            #(No of a node, amount of bridges that node is a part of)
            breaking_points.append((i, points[i]))

    # print(B)
    # print(breaking_points)

    return B
