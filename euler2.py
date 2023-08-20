from queue import PriorityQueue

def Euler(G, start):

    #G - adj. list
    #multigraf skierowany
    n = len(G)
    last_index = [0 for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for v in G[i]:
            M[i][v] += 1

    cycle = []

    def DFSVisit(node):

        last = last_index[node]
        # print("wchodze do node", node, "zaczynam od", last)

        for k in range(last, n):

            if M[node][k] > 0:
                M[node][k] -= 1
                last = k
                last_index[node] = last
                DFSVisit(k)

        last_index[node] = last
        cycle.append(node)

    DFSVisit(start)
    cycle.reverse()
    return cycle
