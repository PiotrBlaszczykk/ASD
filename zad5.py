#Piotr Błaszczyk
#
#Zaczynam od zamienienia danych z E na listę sąsiedztwa.
#Kolejnym krokiem jest stworzenie czarnej dziury, która jest połączona z każdą planetą ze zbioru S
#gdzie waga każdego połącznia wynosi 0.
#Następnie odpalam algorytm dijkstry, gdzie startową planetą jest a
#Program zostanie przerwany, gdy dotrę do planey b. Jeżeli algortym dijkstry się skończy
#i nie dotarłem po drodze do planety b, to znaczy, że połącznie z a do b nie istnieje i zwracam None
#Złożoność czasowa algorytmu to O( (len(E)) * logn )

from zad5testy import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):

    # if a in S and b in S:
    #     return 0

    nodes = [[] for _ in range(n + 1)]

    for i in range(len(E)):

        nodes[E[i][0]].append((E[i][1], E[i][2]))
        nodes[E[i][1]].append((E[i][0], E[i][2]))

    for i in range(len(S)):

        nodes[n].append((S[i], 0))
        nodes[S[i]].append((n, 0))

    visited = [False for _ in range(n + 1)]
    D = [float('inf') for _ in range(n + 1)]
    D[a] = 0
    Q = PriorityQueue()
    Q.put((0, a))

    while Q.empty() == False:

        curr_dist, curr_node = Q.get()

        if curr_node == b:
            return D[b]

        if visited[curr_node] is False:

            visited[curr_node] = True

            for somsiad, d in nodes[curr_node]:

                if visited[somsiad] is False:

                    new_dist = curr_dist + d

                    if new_dist < D[somsiad]:

                        D[somsiad] = new_dist
                        Q.put((new_dist, somsiad))

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )