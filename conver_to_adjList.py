def convert_to_adjList(E):

    #E: [(node1, node2, weight), ...]

    n = float('-inf')

    for i in range(len(E)):

        if E[i][0] > n:
            n = E[i][0]
        if E[i][1] > n:
            n = E[i][1]

    n += 1
    G = [[[]] for _ in range(n)]

    for i in range(len(E)):

        G[E[i][0]][0].append((E[i][1], E[i][2]))
        G[E[i][1]][0].append((E[i][0], E[i][2]))

    return G
