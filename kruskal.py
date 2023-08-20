def Kruskal(G):

    class Node:
        def __init__(self, value):
            self.value = value
            self.parent = self
            self.rank = 0

    def find(x):
        if x.parent != x:
            x.parent = find(x.parent)

        return x.parent

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return False

        if x.rank > y.rank:
            y.parent = x

        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1
        return True


    n = len(G)
    visited = [False for _ in range(n)]
    E = []
    for i in range(n):
        visited[i] = True
        for edge in G[i]:
            if not visited[edge[0]]:
                E.append((edge[1], i, edge[0]))

    #E: (waga, u, v)
    E.sort(key = lambda x:x[0])

    V = [None for _ in range(n)]
    for i in range(n):
        V[i] = Node(i)

    suma = 0
    MST = []

    for i in range(len(E)):
        waga, u, v = E[i]

        if union(V[u], V[v]):
            suma += waga
            MST.append(E[i])

        if len(MST) == n - 1:
            return suma
