from collections import deque


def Euler(G, start):
    # G - adj. list

    n = len(G)
    last_index = [0 for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for v in G[i]:
            M[i][v] = 1

    cycle = []

    def DFSVisit(node):

        last = last_index[node]
        # print("wchodze do node", node, "zaczynam od", last)

        for k in range(last, n):

            if M[node][k] == 1:
                M[node][k] = 0
                M[k][node] = 0
                last = k
                last_index[node] = last
                DFSVisit(k)

        last_index[node] = last
        cycle.append(node)

    DFSVisit(start)
    return cycle


def recursion_proof_euler(G, start):
    # G - adj. list
    # recursion proof
    n = len(G)
    last_index = [0 for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for v in G[i]:
            M[i][v] = 1

    cycle = []
    Q = deque()

    def DFSVisit(node):

        last = last_index[node]
        # print("wchodze do node", node, "zaczynam od", last)

        for k in range(last, n):

            last = last_index[node]
            if M[node][k] == 1:
                M[node][k] = 0
                M[k][node] = 0
                last = k + 1
                last_index[node] = last
                Q.append(node)
                Q.append(k)
                return None

        # print("wychodze z node", node)
        last_index[node] = last
        cycle.append(node)

    Q.append(start)
    while not len(Q) == 0:
        DFSVisit(Q.pop())

    return cycle
