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

    def haszuj(napis):

        kod = ord(napis[0]) + ord(napis[-1])
        kod *= len(napis)
        kod = kod**2 - ord(napis[0])
        kod = kod % n

        return kod

    def dodaj(tab, napis):

        index = haszuj(napis)

        if tab[index][0] is None:
            tab[index][0] = [napis, 1]
            return 1

        else:

            for i in range(len(tab[index])):

                if tab[index][i][0] == napis:
                    tab[index][i][1] += 1
                    return tab[index][i][1]

            tab[index].append([napis, 1])
            return 1

    for i in range(len(T)):

        T[i] = kwadratuj(T[i])

    mapa = [[None] for _ in range(n)]

    wynik = 1
    for i in range(n):

        score = dodaj(mapa, T[i])

        if score > wynik:
            wynik = score

    return wynik


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
