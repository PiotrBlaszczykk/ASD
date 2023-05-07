from queue import PriorityQueue

def rozmnozona_dijkstra(G, start, x):
    # G - adj. list
    # x - max path length in terms of edges

    x += 1
    n = len(G)

    n = len(G)
    visited = [[False for _ in range(x)] for _ in range(n)]
    D = [[float('inf') for _ in range(x)] for _ in range(n)]

    for i in range(x):
        D[start][i] = 0

    Q = PriorityQueue()
    Q.put((0, (start, 0)))

    while not Q.empty():

        curr_dist, node = Q.get()

        curr_node = node[0]
        odw = node[1]

        if not visited[curr_node][odw] and odw < (x - 1):

            visited[curr_node][odw] = True

            for neighbour, d in G[curr_node]:

                if not visited[neighbour][odw + 1]:

                    new_dist = curr_dist + d

                    if new_dist < D[neighbour][odw + 1]:
                        D[neighbour][odw + 1] = new_dist
                        Q.put((new_dist, (neighbour, odw + 1)))

    return D
