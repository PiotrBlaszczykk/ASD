def Euler(G, start):

    #G - adj. list

    n = len(G)
    last_index = [0 for _ in range(n)]
    n = len(G)
    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):

        for v in G[i]:

            M[i][v[0]] = 1
            M[v[0]][i] = 1

    parent = [None for _ in range(n)]
    cycle = []

    def DFSVisit(node):

        last = last_index[node]
        # print("wchodze do node", node, "zaczynam od", last)

        for k in range(last, n):

            if M[node][k] == 1:
                M[node][k] = 0
                M[k][node] = 0
                last = k
                last_index[node] = last
                DFSVisit(k)

        last_index[node] = last
        cycle.append(node)

    DFSVisit(start)

    return cycle
