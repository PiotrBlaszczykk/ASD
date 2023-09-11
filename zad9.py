# Piotr Błaszczyk
#
# Algorytm tworzy 3 kolejki Priorytetowe, służą one do tego aby przyspieszyć rozpatrywanie przedziałów
# Najpierw każdy parking przedstawiam jako tablice 4 elementową:
# tab[i] = [ odległość od A, opłata za parkig, najmniejszy koszt dotarcia i wyjechania z tego parkingu, koszt z wyjątkiem ]
# sortuje parkingi po odległości.
# iteruje przez każdy parking, podczas sprawdzania parkingu i biore z "miniętych" parkingów w odległości T i 2T ten
# parking, który ma najmniejszy koszt dojechania. Aby nie robić zakażdym razem kolejnej iteracji w szukaniu parkingów
# w odległości T i 2T ( co by prowadziło do "skwadracenia się" algorytmu ) wykorzystuję kolejkę priorytetową. Biore
# za każdym razem parking z najmniejszym kosztem, więc kluczem w kolejce jest koszt dotarcia
# Na potrzeby zadania potrzeba 3 kolejek, pierwsza kolejka do wyliczenia koszta dotarcia bez wykorzystania wyjątku
# Druga kolejka będzie potrzebna do wykorzystania wyjątku, ale z parkingów w tej kolejce jescze nie jechaliśmy z wyjątkiem
# W trzeciej kolejce mamy parkingi, w których wcześniej wykorzystaliśmy wyjątek
# Złożonośc czasowa programu to O(nlogn)

from zad9testy import runtests
from queue import PriorityQueue

def min_cost(O, C, T, L):
    inf = float('inf')
    n = len(O)
    tab = [None for _ in range(n + 1)]
    tab[0] = [0, 0, 0, 0]
    for i in range(n):
        tab[i + 1] = [O[i], C[i], None, None]
    tab.sort(key = lambda x:x[0])
    tab.append([L, 0, inf, None, None])
    n += 2


    Q = PriorityQueue()
    Q.put((0 ,tab[0]))

    Q2 = PriorityQueue() # z wyjatkiuem
    Q3 = PriorityQueue() # z wyjatkiem, ale jeszcze nie skorzystalismy
    Q3.put((0, tab[0]))

    for i in range(1, n):

        d = inf

        while d > (2 * T):

            cost, parking = Q3.get()
            d = tab[i][0] - parking[0]

        tab[i][3] = cost + tab[i][1]
        Q3.put((cost, parking))
        tab[1][3] = tab[i][3]
        Q2.put((tab[i][3], tab[i]))

        d = inf
        while d > T:

            cost, parking = Q.get()
            d = tab[i][0] - parking[0]

        tab[i][2] = cost + tab[i][1]
        Q.put((cost, parking))
        Q.put((tab[i][2], tab[i]))
        Q3.put((tab[i][2], tab[i]))

        d = inf
        while d > T:

            cost, parking = Q2.get()
            d = tab[i][0] - parking[0]

        tab[i][3] = cost + tab[i][1]
        Q2.put((cost, parking))
        Q2.put((tab[i][3], tab[i]))

    wynik = tab[-1][3]
    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)
