from egzP3btesty import runtests
from queue import PriorityQueue


def lufthansa(G):

    n = len(G)
    start = 0
    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    D = [float('-inf') for _ in range(n)]
    D[start] = 0
    visited = [False for _ in range(n)]
    suma = 0

    Q.put((0, start))
    total = 0

    for node in G:
        for edge in node:
            total += edge[1]

    total = total // 2

    while not Q.empty():

        d, curr_node = Q.get()
        visited[curr_node] = True

        for neighbour, distance in G[curr_node]:

            if not visited[neighbour]:

                if distance > D[neighbour]:
                    D[neighbour] = distance
                    parent[neighbour] = curr_node
                    Q.put((-distance, neighbour))

    for i in range(n):
        suma += D[i]

    extra = -1

    for i in range(n):

        node = G[i]

        for edge in node:

            vertex = edge[0]
            weight = edge[1]

            if parent[i] != vertex and parent[vertex] != i:
                if weight > extra:
                    extra = weight

    suma += extra

    return total - suma

runtests ( lufthansa, all_tests= True )
