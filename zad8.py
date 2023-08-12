#Piotr Błaszczyk
#
#Algorytm zachłanny. Najpierw zrobiłem funkcje pomocniczą "zlicz_rope", która oblicza objętość całej plamy.
#zlicz_rope wykorzystuje do tego rekurencje. Jest to obliczeniowo "najcięższy" fragment algorytmu o złożoności O(m*n).
#a efekcie mam tablice "plamy" o długości m, gdzie wartości różne od 0 to ile ropy można zebrać z miejsca na którym stoimy
#Teraz w sposób zachłanny "dojeżdżamy"  najdalej jak się przy zebranym paliwie. Jak zatrzymaliśmy się na polu d < m - 1,
#to zbieramy największą możliwą plamę którą minęliśmy po drodze i jedziemy dalej aż dojedziemy do końca. W celu
#zebrania największej minętej plamy, wtedy kiedy jedziemy i jesteśmy na kolejnych polach tablicy "plamy", to gdy napotkamy
#jakąś plame to dodajemy ją do kolejki priorytetowej. Można o tym pomyśleć w ten sposób, że jedziemy najdalej jak się da,
#a w momencie gdy skończy nam się paliwo to wysiadamy z cysterny i idziemy piszo po największą plamę jaką minęliśmy.
#Złożoność czasowa programu to O(m*n)

from zad8testy import runtests
from queue import PriorityQueue

def plan(T):

    n = len(T)
    m = len(T[0])

    def zlicz_rope(x):

        ropa = []

        def rek(u, v):

            ropa.append(T[u][v])
            T[u][v] = 0

            if u < n - 1:

                if T[u + 1][v] != 0:
                    rek(u + 1, v)

            if u > 0:

                if T[u - 1][v] != 0:
                    rek(u - 1, v)

            if v < m - 1:

                if T[u][v + 1] != 0:
                    rek(u, v + 1)

            if v > 0:

                if T[u][v - 1] != 0:
                    rek(u, v - 1)

        rek(0, x)

        wynik = 0

        for i in range(len(ropa)):

            wynik += ropa[i]

        return wynik

    plamy = [0 for _ in range(m)]

    for i in range(m):

        if T[0][i] != 0:

            rupa = zlicz_rope(i)
            plamy[i] = rupa

    postoje = 0
    d = 0
    Q = PriorityQueue()
    Q.put(plamy[0] * -1)

    while d < m - 1:

        postoje += 1
        bak = Q.get() * -1

        for i in range(bak):

            d += 1

            if d == m - 1:
                return postoje

            if plamy[d] != 0:

                Q.put(plamy[d] * -1)

    return postoje

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
