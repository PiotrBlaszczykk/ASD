from zad2testy import runtests
from collections import deque

def BFS(G, start):
    # G - adj. list

    n = len(G)
    visited = [False for _ in range(n)]

    Q = deque()
    visited[start] = True

    Q.append(start)

    while len(Q) != 0:

        u = Q.popleft()
        for v in G[u]:

            if not visited[v]:
                visited[v] = True
                Q.append(v)

    return visited

def convert_to_list(M):

    n = len(M)
    V = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):

            if M[i][j] == 1:

                V[i].append(j)

    return V

def remove_and_convert_to_list(M, removed):

    n = len(M)
    V = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):

            if M[i][j] == 1:

                if i != removed and j != removed:

                    V[i].append(j)

    return V


def check(arr):
    for p in range(len(arr)):
        if arr[p] == False:
            return True
    return False

def bridges(G):

    # G - adj. list

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    children = [[] for _ in range(n)]
    low = [None for _ in range(n)]
    time = 0
    B = []

    parent[0] = 0

    def DFSVisit(node):

        nonlocal time
        #print("odwiedzam node:", node, "time =", time)


        d[node] = time
        low[node] = time

        time += 1
        visited[node] = True

        for neighbour in G[node]:

            if visited[neighbour] and parent[node] != neighbour:

                #print("sprawdzam krawdz wsteczna", node, neighbour)
                low[node] = min(low[node], d[neighbour])
                #print("low node", node, "to", low[node])

        for neighbour in G[node]:

            if not visited[neighbour]:
                parent[neighbour] = node
                children[node].append(neighbour)
                DFSVisit(neighbour)
                low[node] = min(low[node], low[neighbour])
                #print("wracam z", neighbour, "low node", node, "to", low[node])

        if node != 0:
            low[parent[node]] = min(low[parent[node]], low[node])

        if d[node] == low[node] and node != 0:

            x = min(node, parent[node])
            y = max(node, parent[node])
            B.append((x, y))


    for node in range(n):

        if not visited[node]:
            DFSVisit(node)

    articulation_points = []

    if len(children[0]) > 1:
        articulation_points.append(0)

    for node in range(1, n):

        for child in children[node]:

            if low[child] >= d[node]:

                articulation_points.append(node)
                break

    #return low
    #return articulation_points
    return articulation_points

def breaking(G):

    n = len(G)

    wynik = 0
    vertex = None

    nodes = convert_to_list(G)

    points = bridges(nodes)

    for node in points:

        niespojne = -1
        nodes = remove_and_convert_to_list(G, node)
        checked = [False for _ in range(n)]
        checked[node] = True


        while check(checked):

            niespojne += 1
            k = 0
            while checked[k] == True:
                k+=1

            visited = BFS(nodes, k)

            for j in range(n):

                if visited[j] == True:

                    checked[j] = True

        if niespojne > wynik:

            wynik = niespojne
            vertex = node

    return vertex


runtests( breaking )
