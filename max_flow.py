from zad9testy import runtests
from collections import deque

def Edmons_Karp(G, s, a, b):

    n = len(G)
    M = [[0 for _ in range(n)] for _ in range(n)]
    parent = [None for _ in range(n)]
    flow1 = 0

    for i in range(n):

        for neighbour, w in G[i]:
            M[i][neighbour] = w


    def BFS(bool):

        Q = deque()
        visited = [False for _ in range(n)]

        visited[s] = True
        Q.append(s)

        while len(Q) != 0:
            u = Q.popleft()

            for v in range(n):
                if not visited[v] and M[u][v] != 0:
                    visited[v] = True
                    parent[v] = u
                    Q.append(v)

        if bool:
            return visited[a]
        else:
            return visited[b]

    while BFS(True):

        new_flow = float('inf')
        u = a
        while u != s:
            new_flow = min(new_flow, M[parent[u]][u])
            u = parent[u]

        flow1 += new_flow
        v = a

        while v != s:
            u = parent[v]
            M[u][v] -= new_flow
            M[v][u] += new_flow
            v = u

    flow2 = 0
    while BFS(False):

        new_flow = float('inf')
        u = b
        while u != s:
            new_flow = min(new_flow, M[parent[u]][u])
            u = parent[u]

        flow2 += new_flow
        v = b

        while v != s:
            u = parent[v]
            M[u][v] -= new_flow
            M[v][u] += new_flow
            v = u

    return flow1 + flow2

def maxflow( G,s ):

    n1 = max(G, key=lambda x:x[0])
    n2 = max(G, key=lambda x:x[1])
    n = max(n1[0], n2[1])

    M = [[] for _ in range(n + 1)]

    for u, v, weight in G:

        M[u].append((v, weight))

    G = M
    wynik = -1

    for i in range(n):

        for j in range(i + 1, n):

            if i != s and j != s and i != j:

                wynik = max(wynik, Edmons_Karp(G, s, i, j))


    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )
