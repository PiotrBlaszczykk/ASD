from egzP5btesty import runtests

def bridges(G):

    # G - adj. list

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    children = [[] for _ in range(n)]
    low = [None for _ in range(n)]
    time = 0

    parent[0] = 0

    def DFSVisit(node):

        nonlocal time
        d[node] = time
        low[node] = time

        time += 1
        visited[node] = True

        for neighbour in G[node]:

            if visited[neighbour] and parent[node] != neighbour:
                low[node] = min(low[node], d[neighbour])

        for neighbour in G[node]:

            if not visited[neighbour]:
                parent[neighbour] = node
                children[node].append(neighbour)
                DFSVisit(neighbour)
                low[node] = min(low[node], low[neighbour])

        if node != 0:
            low[parent[node]] = min(low[parent[node]], low[node])


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

    return len(articulation_points)

def koleje ( B ):

    n = -1
    for u, v in B:
        if u > n:
            n = u
        if v > n:
            n = v
    n += 1

    G = [[] for _ in range(n)]
    pom = [[] for _ in range(n)]

    for u, v in B:
        pom[u].append(v)
        pom[v].append(u)

    for i in range(n):
        pom[i].sort()

    for i in range(n):

        G[i].append(pom[i][0])
        for j in range(1, len(pom[i])):

            if pom[i][j] != G[i][-1]:
                G[i].append(pom[i][j])

    return bridges(G)

runtests ( koleje, all_tests= True)
