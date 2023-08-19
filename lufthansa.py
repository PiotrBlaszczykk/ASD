from queue import PriorityQueue


def lufthansa(G):
    n = len(G)

    E1 = []

    for node in G:

        for edge in node:
            E1.append(edge[1])

    E1.sort(reverse=True)
    E = []

    for i in range(len(E1) // 2):
        E.append(E1[i * 2])

    # print(E)

    start = 0

    # Algorytm Prima
    # G - adj list

    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    D = [float('-inf') for _ in range(n)]
    D[start] = 0
    visited = [False for _ in range(n)]
    suma = 0

    najwieksza_krawedz = float('inf')

    Q.put((0, start))

    while not Q.empty():

        d, curr_node = Q.get()
        visited[curr_node] = True

        for neighbour, distance in G[curr_node]:

            if not visited[neighbour]:

                if distance > D[neighbour]:
                    D[neighbour] = distance
                    parent[neighbour] = curr_node
                    Q.put((-distance, neighbour))

    # print(E)
    # print(D)

    D.sort(reverse=True)

    n = 0
    k = 0
    wynik = 0

    while n < len(E):

        while E[n] != D[k]:

            wynik += E[n]
            n += 1

            if n == len(E):
                break

        if n == len(E):
            break

        E[n] = 0

        n += 1
        k += 1
        if k == len(D):
            break

    x = max(E)

    wynik -= x

    return wynik
