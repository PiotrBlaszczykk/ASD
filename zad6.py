#Piotr Błaszczyk
#
#Szybko można zauważyć, że problem sprowadza się do grafu dwudzielnego, gdzie trzeba znaleźć liczność maksymalnego skojarznia
#Najszybszy będzie tuaj algorytm Hopcroft–Karp'a
#Problem jest o tyle ułatwiony, że nie musimy tworzyć pełnej reprezentacji grafu np listy sąsiedztwa czy macierzy
#Bo wystarczą nam tutaj tylko lista sąsiedztwa wierzchołków z pierwszego zbioru, która jest od razu podana jako M
#tablica wolne_wierchołki ma na początku wartości -1, aby można było odróżnić od wierzchołków, co mają numery od 0 do n
#Funkcja do szukania scieżek powiększających bazuje na DFS.
#
#Ostatecznie liczebność skojarzenia to ilość wierzchołków, która "jest w parze". Algorytm ma złożoność czasową O(E * sqrt(V))

from zad6testy import runtests

def binworker( M ):

    n = len(M)
    wolne_wierzcholki = [-1 for _ in range(n)]

    def czy_ma_sciezkePow(node, visited):

        for sasiad in M[node]:

            if visited[sasiad] == False:

                visited[sasiad] = True

                if wolne_wierzcholki[sasiad] == -1 or czy_ma_sciezkePow(wolne_wierzcholki[sasiad], visited) == True:

                    wolne_wierzcholki[sasiad] = node
                    return True

        return False


    for i in range(n):

        visited = [False for _ in range(n)]
        czy_ma_sciezkePow(i, visited)


    skojarzenie = 0

    for node in wolne_wierzcholki:

       if node != -1:

           skojarzenie += 1


    return skojarzenie


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
