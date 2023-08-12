from zad4testy import runtests

def sus(x):
    return x[2]

def select_buildings(T,p):

    n = len(T)

    for i in range(n):

        T[i] = ((T[i][0] * (T[i][2] - T[i][1])), T[i][1], T[i][2], T[i][3], i)

    T = sorted(T, key = sus)

    D = [[None for _ in range(p + 1)] for _ in range(n)]
    budowa = [[None for _ in range(p + 1)] for _ in range(n)]
    parent = [[None for _ in range(p + 1)] for _ in range(n)]

    for i in range(p + 1):

        if T[0][3] > i:
            D[0][i] = 0
            budowa[0][i] = False
        else:
            D[0][i] = T[0][0]
            budowa[0][i] = True

    kolizje = [[] for _ in range(n)]

    for i in range(1, n):

        for j in range(1, i + 1):

            if T[i - j][2] >= T[i][1]:
                kolizje[i].append(i - j)
            else:
                break

    for i in range(1, n):

        pojemnosc = T[i][0]
        cena = T[i][3]

        for j in range(p + 1):

            if cena > j:
                D[i][j] = D[i - 1][j]
                budowa[i][j] = False
                continue

            if len(kolizje[i]) == 0:
                ostatni = i - 1
            else:
                ostatni = kolizje[i][-1] - 1

            if ostatni == -1:
                budujemy = pojemnosc
            else:
                budujemy = D[ostatni][j - cena] + pojemnosc

            nie_budujemy = D[i - 1][j]

            if budujemy > nie_budujemy:
                budowa[i][j] = True
                D[i][j] = budujemy
                parent[i][j] = (ostatni, j - cena)

            else:
                budowa[i][j] = False
                D[i][j] = nie_budujemy



    print("$$$", D[n - 1][p])

    wynik = []
    budynek = (n - 1, p)

    while budynek is not None:

        x, y = budynek[0], budynek[1]
        if x == -1:
            break

        if budowa[x][y]:

            wynik.append(T[x][4])
            budynek = parent[x][y]

        else:

            budynek = (x - 1, y)

    wynik.sort()
    return wynik

runtests( select_buildings )
