from kol2testy import runtests

def czy_spojny(G):

    #DFS
    n = len(G)
    visited = [False for _ in range(n)]

    def visit(node):

        visited[node] = True
        for neighbour in G[node]:
            if not visited[neighbour]:
                visit(neighbour)

    visit(0)
    for i in range(n):
        if not visited[i]:
            return False

    return True

def add_edge(G, u ,v):

    G[u].append(v)
    G[v].append(u)

def remove_edge(G, u, v):

    G[v].pop(0)
    G[u].pop(0)

def beautree(G):

    n = len(G)
    visited = [False for _ in range(n)]
    E = []
    for i in range(n):
        visited[i] = True
        node = G[i]
        for v, weight in node:
            if not visited[v]:
                E.append((weight, i, v))

    E.sort(key = lambda x:x[0])
    suma = 0

    G2 = [[] for _ in range(n)]
    for i in range(n - 2):

        waga, u, v = E[i]
        suma += waga
        add_edge(G2, u, v)

    for i in range(n - 2, len(E)):

        waga, u, v = E[i]
        suma += waga
        add_edge(G2, u, v)

        if czy_spojny(G2):
            return suma
        else:
            waga, u, v = E[i - n + 2]
            suma -= waga
            remove_edge(G2, u, v)

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
