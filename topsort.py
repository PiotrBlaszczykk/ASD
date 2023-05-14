def topsort(G):

    # G - adj. list
    n = len(G)
    visited = [False for _ in range(n)]

    tab = []

    def DFSVisit(node):

        visited[node] = True

        for neighbour in G[node]:

            if not visited[neighbour]:
                DFSVisit(neighbour)

        tab.append(node)

    for i in range(n):

        if not visited[i]:
            DFSVisit(i)

    tab.reverse()
    return tab
