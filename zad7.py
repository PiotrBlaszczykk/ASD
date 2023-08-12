from zad7testy import runtests

def maze( L ):

    n = len(L)
    D = [[None for _ in range(n)] for _ in range(n)]
    inf = float('-inf')

    flag = False
    for i in range(n):

        if L[n - 1 - i][n - 1] == "#":
            flag = True

        if flag:
            D[n - i - 1][n - 1] = inf
        else:
            D[n - i - 1][n - 1] = i


    def go(x, y):

        if D[x][y] is not None:
            return D[x][y]

        if L[x][y] == "#":
            D[x][y] = inf
            return inf

        #d = [None for _ in range(n)]
        #d[x] = 1

        wynik = go(x, y + 1) + 1

        pointer = 1
        while x - pointer >= 0:

            if L[x - pointer][y] == "#":
                break

            sus = go(x - pointer, y + 1) + pointer + 1
            if sus > wynik:
                wynik = sus

            pointer += 1

        pointer = 1
        while x + pointer < n:

            if L[x + pointer][y] == "#":
                break
            sus = go(x + pointer, y + 1) + pointer + 1
            if sus > wynik:
                wynik = sus

            pointer += 1

        D[x][y] = wynik
        return wynik

    wynik = inf

    go(0, 0)

    wynik = D[0][0]

    if wynik == inf:
        return -1
    return wynik



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
