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

        x = Q.get()
        curr_dist = x[0]
        curr_node = x[1]

        if not visited[curr_node]:

            visited[curr_node] = True

            for node in G[curr_node][0]:

                neighbour = node[0]
                d = node[1]

                if not visited[neighbour]:

                    new_dist = curr_dist + d

                    if new_dist < D[neighbour]:

                        D[neighbour] = new_dist
                        Q.put((D[neighbour], neighbour))

    for i in range(n):

        if D[i] == float('inf'):
            D[i] = None

    return D