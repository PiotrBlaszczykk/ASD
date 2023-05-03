#Piotr Błaszczyk
#
#Do rozwiązania problemu użyłem własnej implementacji hash-mapy
#Najpierw jednak użyłem funkcji pomocniczej, która wszystkie równoważne napisy zamienia na ten sam napis
#jeżeli odwrotność napisu wsytępuje wcześniej w porządku leksykograficznym, jest on na takowy zamieniany
#(funkcję nazwałem kwadratuj, bo mi się skojarzyło z tym że x i -x do kwd. jest takie same)
#do haszowania używam ord, haszowanie ma złożonośc O(1), ponieważ nie zależy od długości napisu
#(co prawda jest tam len(napis), ale złożoność len to O(1))
#Tworzę mapę długości n, do haszowania używam na końcu modulo n aby się zmieścić w tablicy.
#Napisy idą pod index tablicy który odpowiada im haszom
#Funkcja dodaj dodaje napis do mapy i od razu zwraca ile razy ten napis już wystąpił, oraz zarządza kolizjami gdy 2 lub
#więcej napisów ottrzyma ten sam hasz
#Złożoność pesymistyczna to O(N^2), jednakże szanse na to że się program "skwadraci" są bardzo małe, wymagałoby to
#aby wszystkie napisy ottrzymały ten sam hasz i były różne. W praktyce złożonośc czasowa jest bliższa O(N), i działa
#szybciej niż przy sortowaniu. Złożoność pamięciowa to O(N)

from zad3testy import runtests

def strong_string(T):

    n = len(T)

    def kwadratuj(napis):

        if napis[::-1] < napis:

            return napis[::-1]

        return napis
    #
    # def merge_sort(tab):
    #     def merge(tab1, tab2):
    #         pointer1 = 0
    #         pointer2 = 0
    #         tab3 = [0] * (len(tab1) + len(tab2))
    #         for i in range(len(tab1) + len(tab2)):
    #             if tab1[pointer1] < tab2[pointer2]:
    #                 tab3[i] = tab1[pointer1]
    #                 pointer1 += 1
    #             else:
    #                 tab3[i] = tab2[pointer2]
    #                 pointer2 += 1
    #             if pointer1 == len(tab1):
    #                 i += 1
    #                 while pointer2 < len(tab2):
    #                     tab3[i] = tab2[pointer2]
    #                     pointer2 += 1
    #                     i += 1
    #                 del tab1
    #                 del tab2
    #                 return tab3
    #             if pointer2 == len(tab2):
    #                 i += 1
    #                 while pointer1 < len(tab1):
    #                     tab3[i] = tab1[pointer1]
    #                     pointer1 += 1
    #                     i += 1
    #                 del tab1
    #                 del tab2
    #                 return tab3
    #         del tab1
    #         del tab2
    #         return tab3
    #
    #     def rek(arr):
    #         if len(arr) == 1:
    #             return arr
    #         pivot = len(arr) // 2
    #         arr1 = rek(arr[:pivot])
    #         arr2 = rek(arr[pivot:])
    #         return merge(arr1, arr2)
    #
    #     return rek(tab)
    #
    for i in range(n):
        T[i] = kwadratuj(T[i])
    #
    # T = merge_sort(T)

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

        for i in range(N - 1, 0, -1):
            A[0], A[i] = A[i], A[0]
            heapify(A, 0, i)

    heap_sort_wyk(T)

    N = n
    n = 0
    wynik = 1


    while n < N:

        x = T[n]
        score = 0
        while T[n] == x:

            score += 1
            n += 1

            if n == N:

                if score > wynik:
                    return score
                return wynik

        if score > wynik:
            wynik = score

    return wynik

    # def koduj(napis):
    #
    #     kod = ord(napis[0]) + ord(napis[-1])
    #     kod *= len(napis)
    #     kod = kod**2 - ord(napis[0])
    #     kod = kod % n
    #
    #     return kod
    #
    # def dodaj(tab, napis):
    #
    #     index = koduj(napis)
    #
    #     if tab[index][0] is None:
    #         tab[index][0] = [napis, 1]
    #         return 1
    #
    #     else:
    #
    #         for i in range(len(tab[index])):
    #
    #             if tab[index][i][0] == napis:
    #                 tab[index][i][1] += 1
    #                 return tab[index][i][1]
    #
    #         tab[index].append([napis, 1])
    #         return 1
    #
    # for i in range(len(T)):
    #
    #     T[i] = kwadratuj(T[i])
    #
    # napisy = [[None] for _ in range(n)]
    #
    # wynik = 1
    # for i in range(n):
    #
    #     score = dodaj(napisy, T[i])
    #
    #     if score > wynik:
    #         wynik = score
    #
    # return wynik


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )

