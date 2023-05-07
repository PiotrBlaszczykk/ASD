from egzP1btesty import runtests
from queue import PriorityQueue

def convert_to_adjList(E):

    #E: [(node1, node2, weight), ...]

    n = float('-inf')

    for i in range(len(E)):

        if E[i][0] > n:
            n = E[i][0]
        if E[i][1] > n:
            n = E[i][1]

    n += 1
    G = [[] for _ in range(n)]

    for i in range(len(E)):

        G[E[i][0]].append((E[i][1], E[i][2]))
        G[E[i][1]].append((E[i][0], E[i][2]))

    return G

def turysta( G, D, L ):

    G = convert_to_adjList(G)
    n = len(G)

    start = D
    end = L

    n = len(G)
    visited = [[False for _ in range(5)] for _ in range(n)]
    D = [[float('inf') for _ in range(5)] for _ in range(n)]

    for i in range(5):

        D[start][i] = 0

    Q = PriorityQueue()
    Q.put((0, (start, 0)))

    while not Q.empty():

        curr_dist, node = Q.get()

        curr_node = node[0]
        odw = node[1]

        if curr_node == end and odw == 4:
            return curr_dist


        if not visited[curr_node][odw] and odw < 4:

            visited[curr_node][odw] = True

            for neighbour, d in G[curr_node]:

                if not visited[neighbour][odw + 1]:

                    new_dist = curr_dist + d

                    if new_dist < D[neighbour][odw + 1]:
                        D[neighbour][odw + 1] = new_dist
                        Q.put((new_dist, (neighbour, odw + 1)))


    return D[end][4]


runtests ( turysta )
