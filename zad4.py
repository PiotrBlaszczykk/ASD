#Piotr Błaszczyk
#
#Za pomocą BFS szukam najkrótszej ścieżki od s do t ( wierzochłki scieżki są zapisane )
#potem za pomocą BFS sprawdzam osobno dla każdej krawędzi ścieżki,
#czy po jej usunięciu długość najkrótszej ścieżki się wydłuży, jeśli tak, to zwracam tą krawęź jako wynik
#Jeżeli przeiteruje przez wszystkie krawędzie bez wydłużenia ścieżki, to zwracam None
#dodatkowo sprawdzam na początku, czy ściężka od s do t w ogóle istnieje
#program ma złożoność O(V*(V + E))

from collections import deque
from zad4testy import runtests

def longer( G, s, t ):

    def BFS():

        n = len(G)
        visited = [False for _ in range(n)]
        parent = [None for _ in range(n)]
        d = [-1 for _ in range(n)]
        Q = deque()
        d[s] = 0
        visited[s] = True

        Q.append(s)
        min_sciezka = None

        while not len(Q) == 0:
            u = Q.popleft()
            for v in G[u]:

                if not visited[v]:
                    d[v] = d[u] + 1
                    if min_sciezka != None and d[v] > min_sciezka:

                        return (d, parent, visited)

                    if v == t:
                        min_sciezka = d[v]

                    parent[v] = u
                    visited[v] = True
                    Q.append(v)

        return (d, parent, visited)

    d, parent, visited = BFS()
    #odtwarzamy ciezki z s do t

    if visited[t] == False:
        return None

    x = t
    sciezka = [t]

    while x != s:
        sciezka.append(parent[x])
        x = parent[x]

    najkrotsza = d[t]


    for node in sciezka:
        if parent[node] is not None:

            usiniety = [node, parent[node]]

            G[parent[node]].remove(node)


            dprim, parentprim, visitedprim = BFS()

            if visitedprim[t] == False:

                return usiniety


            if dprim[t] > d[t]:

                return usiniety
            G[parent[node]].append(node)

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
