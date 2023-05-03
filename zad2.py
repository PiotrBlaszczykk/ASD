#Piotr Błaszczyk
#
#Bierzemy k największych "górek" śniegu. Kolejność w której zbierzemy śnieg nie ma znaczenia.
#śnieg się wszędzie topi równomiernie, więc wzięcie wcześniej mniejszej górki nie sprawi że zaoszczędzimy więcej śniegu
#Z racji że kolejność nie ma znacznienia, to zawsze istnieje sposób dojechania z W or E, tak aby nie stopić pozostałych
#górek z k. Z racji że bierzemy tylko k górek, gdzie k <= n, to nie musimy się martwić o stopienie śniegu,
#który i tak by stopniał zanim moglibyśmy go zebrać
#
#aby znaleźć k największych górek użyłem gotową implementację algorytmu sortowania heap sort, która była pokazana na wykładzie.
#Heap sort jest tutaj lepszy, poniweważ pod koniec
#algorytmu sortowania, bierzemy po kolei największe elementy i dajemy je na koniec. Tutaj jednak nie musimy posortować całej tablicy,
#poniważ po k dniach pozostały śnieg się już stopi, więc nie robi nam to różnicy czy było tam k-1 czy 0 śniegu, zatem
#sortowanie pozostałych n - k elementów to strata czasu. Zatem sumujemy zebrany śnieg ( z uwagą na topnienie ) z k pierwszych dni
#gdy ilość pierowtnego śniegu pomniejszona o k jest mniejsza bądź równa 0, wiemy, że pozostały śnieg się już stopił i przerywamy algorytm
#Złożonośc czasowa to O(nlogn), ponieważ heap sort ma taką złożoność, a złośonośc pamięciowa to O(1)

from zad2testy import runtests

def snow( S ):

    def heap_sort_wyk(A):

        def left(n):
            return 2 * n + 1

        def right(n):
            return 2 * n + 2

        def parent(n):
            return (n - 1) // 2

        def heapify(A, i, n):

            l = left(i)
            r = right(i)
            max_ind = i

            if l < n and A[l] > A[max_ind]:
                max_ind = l
            if r < n and A[r] > A[max_ind]:
                max_ind = r

            if max_ind != i:
                A[i], A[max_ind] = A[max_ind], A[i]
                heapify(A, max_ind, n)

        def build_heap(A):
            n = len(A)

            for i in range(parent(n - 1), -1, -1):
                heapify(A, i, n)

        N = len(A)
        build_heap(A)

        wynik = 0
        dzien = 0
        snieg = 0

        for i in range(N - 1, 0, -1):
            snieg = A[0] - dzien

            if snieg <= 0:
                return wynik

            else:
                wynik += snieg
                dzien += 1

            A[0], A[i] = A[i], A[0]
            heapify(A, 0, i)

        return wynik

    snieg_total = heap_sort_wyk(S)

    return snieg_total


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
