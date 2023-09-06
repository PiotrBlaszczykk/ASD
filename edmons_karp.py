from collections import deque

def Edmons_Karp(G, s, t):

    n = len(G)
    M = [[0 for _ in range(n)] for _ in range(n)]
    parent = [None for _ in range(n)]
    flow = 0

    for i in range(n):

        for neighbour, w in G[i]:
            M[i][neighbour] = w


    def BFS():

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

        return visited[t]

    while BFS():

        new_flow = float('inf')
        u = t
        while u != s:
            new_flow = min(new_flow, M[parent[u]][u])
            u = parent[u]

        flow += new_flow
        v = t

        while v != s:
            u = parent[v]
            M[u][v] -= new_flow
            M[v][u] += new_flow
            v = u

    return flow


G = [[(1,5), (2,10), (3,5)], [(4,10)], [(1,15), (5,20)], [(6,10)], [(5,25), (7,10)], [(3,5), (8,30)], [(8,5), (9,10)], [(10, 5)], [(9,5), (10,15)], [(10,10)], []]
#G = [[(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)], [(6, 1), (7, 1), (9, 1)], [(8, 1), (10, 1)], [(6, 1), (8, 1)], [(9, 1)], [(9, 1), (8, 1)], [(11, 1)], [(11, 1)], [(11, 1)], [(11, 1)], [(11, 1)], []]

print("flow: ", Edmons_Karp(G, 0, len(G) - 1))
