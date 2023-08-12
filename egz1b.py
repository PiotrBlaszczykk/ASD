from egz1btesty import runtests

def planets( D, C, T, E ):

    n = len(D)
    inf = float('inf')
    Dynamix = [[inf for _ in range(E + 1)] for _ in range(n)]

    for i in range(E + 1):
        Dynamix[0][i] = i * C[0]

    if T[0][0] != 0:
        Dynamix[T[0][0]][0] = T[0][1]

    for i in range(1, n):

        tele = Dynamix[i][0]
        d = D[i] - D[i - 1]

        if d <= E:
            for j in range(E - d + 1):

                Dynamix[i][j] = Dynamix[i - 1][j + d]

        Dynamix[i][0] = min(tele, Dynamix[i][0])

        if T[i][0] != i:

            Dynamix[T[i][0]][0] = min(T[i][1] + Dynamix[i][0], Dynamix[T[i][0]][0])

        for j in range(1, E + 1):
            Dynamix[i][j] = min(Dynamix[i][j], Dynamix[i][j - 1] + C[i])

    return Dynamix[n - 1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
