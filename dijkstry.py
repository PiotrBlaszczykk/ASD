from queue import PriorityQueue

def dijkstry(G, start):

    #G - adj. list

    n = len(G)
    visited = [False for _ in range(n)]
    D = [float('inf') for _ in range(n)]
    D[start] = 0
    Q = PriorityQueue()
    Q.put((0, start))

    while not Q.empty():

        curr_dist, curr_node = Q.get()

        if not visited[curr_node]:

            visited[curr_node] = True

            for neighbour, d in G[curr_node]:

                if not visited[neighbour]:

                    new_dist = curr_dist + d

                    if new_dist < D[neighbour]:

                        D[neighbour] = new_dist
                        Q.put((new_dist, neighbour))

    return D
