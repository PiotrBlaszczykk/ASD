from zad7ktesty import runtests 

def ogrodnik (T, D, Z, l):

    n = len(D)
    woda = [0 for _ in range(n)]

    m = len(T)
    k = len(T[0])
    def licz_korzenie(x, y, index):

        woda[index] += T[x][y]
        T[x][y] = 0

        if x < m - 1:
            if T[x + 1][y] != 0:
                licz_korzenie(x + 1, y, index)

        if x > 0:
            if T[x - 1][y] != 0:
                licz_korzenie(x - 1, y, index)

        if y < k - 1:
            if T[x][y + 1] != 0:
                licz_korzenie(x, y + 1, index)

        if y > 0:
            if T[x][y - 1] != 0:
                licz_korzenie(x, y - 1, index)

    for i in range(n):
        licz_korzenie(0, D[i], i)

    DP = [[0 for _ in range(l + 1)] for _ in range(n)]

    for i in range(l + 1):

        if woda[0] <= i:

            DP[0][i] = Z[0]

    for i in range(1, n):

        for j in range(l + 1):

            if woda[i] > j:
                DP[i][j] = DP[i - 1][j]
                continue

            podlewamy = Z[i] + DP[i - 1][j - woda[i]]
            nie_podlewamy = DP[i - 1][j]

            DP[i][j] = max(podlewamy, nie_podlewamy)

    return DP[n - 1][l]

runtests( ogrodnik, all_tests=True )
