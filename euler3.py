from collections import deque

def Euler(G, start):

    #G - adj. list
    #multigraf skierowany
    #recursion proof
    n = len(G)
    last_index = [0 for _ in range(n)]
    out = [None for _ in range(n)]
    cycle = []

    for i in range(n):
        out[i] = len(G[i])

    Q = deque()
    #print(G)
    def DFSVisit(node):

        last = last_index[node]
        #print("wchodze do node", node, "zaczynam od", last)
        if out[node] != 0:
            last = last_index[node]
            v = G[node][last]
            out[node] -= 1
            last_index[node] += 1
            Q.append(node)
            Q.append(v)
            return None

        last_index[node] = last
        cycle.append(node)
        #print("wychodze z node", node)

    Q.append(start)
    while not len(Q) == 0:
        DFSVisit(Q.pop())

    DFSVisit(start)
    cycle.reverse()
    cycle.pop(0)
    return cycle
