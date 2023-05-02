def dijkstry_path(G, start, end):

    #G - adj. list
    #if end is not None, then algorithm stops after finding end and returns path with it's length
    #if end is None, returns distance and parent array
    #if end is not None, retuens length and exact path to the end node

    flag = False
    length = None
    if end is not None:
        flag = True

    n = len(G)
    visited = [False for _ in range(n)]
    D = [float('inf') for _ in range(n)]
    D[start] = 0
    Q = PriorityQueue()
    Q.put((0, start))

    parent = [None for _ in range(n)]
    parent[start] = start

    while not Q.empty():

        curr_dist, curr_node = Q.get()
        if flag and curr_node == end:
            length = curr_dist
            break


        if not visited[curr_node]:

            visited[curr_node] = True

            for neighbour, d in G[curr_node]:

                if not visited[neighbour]:

                    new_dist = curr_dist + d

                    if new_dist < D[neighbour]:

                        D[neighbour] = new_dist
                        Q.put((new_dist, neighbour))
                        parent[neighbour] = curr_node

    if flag:

        path = []
        path.append(end)
        node = parent[end]

        if node is None:
            return (None, path)

        while node != start:

            path.append(node)
            node = parent[node]

            if node is None:
                path.reverse()
                return (None, path)


        path.append(start)
        path.reverse()

        return (length, path)

    return (D, parent)
