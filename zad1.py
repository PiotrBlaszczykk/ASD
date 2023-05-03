# Piotr Błaszczyk
#
# program iteruje przez napis długosci n, podczas każdej iteracji szukamy najdłuższego palindromu
# który ma środkową literę s[i], szukanie palindromu odbywa sie przy pomocy dwóch wskaźników, jeden idzie
# prawo a drugi w lewo, za każdym razem sprawdzamy, czy litera wskazywana przez lewy wskaźnik jest taka sama
# jak ta wskazywana przez prawy wskaźnik. wskaźniki idą tak długo aż litery przestaną się zgadzać
# albo jak wyjdziemy poza napis. Mozna zauważyc, że tak znaleziony palindrom zawsze będzie miał
# nieparzystą dlugość, ale jest to ok, ponieważ w poleceniu palindrom ma mieć nieparzystą długość.
# Złożoność czasowa to O(n^2), poniewaz wykonujemy n iteracji, a podczas każdej iteracji
# wykonamy nie wiecej niz n porównań. Złożoność pamięciowa to O(1), ponieważ nie zależy od długości napisu

from zad1testy import runtests


def ceasar( s ):


    N = len(s)

    wynik = 1

    for i in range(1, N):

        n = 1
        licznik = 1

        while i - n >= 0 and i + n < N:

            if s[i - n] == s[i + n]:
                licznik += 2
                n += 1
            else:
                break

        if licznik > wynik:
            wynik = licznik

    return wynik


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
