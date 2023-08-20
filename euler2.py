def Euler(G, start):

    #G - adj. list
    #multigraf skierowany
    n = len(G)
    last_index = [0 for _ in range(n)]
    out = [None for _ in range(n)]
    cycle = []

    for i in range(n):
        out[i] = len(G[i])

    print(G)
    def DFSVisit(node):

        last = last_index[node]
        #print("wchodze do node", node, "zaczynam od", last)
        while out[node] != 0:
            last = last_index[node]
            v = G[node][last]
            out[node] -= 1
            last_index[node] += 1
            DFSVisit(v)

        last_index[node] = last
        cycle.append(node)
        #print("wychodze z node", node)

    DFSVisit(start)
    cycle.reverse()
    return cycle
