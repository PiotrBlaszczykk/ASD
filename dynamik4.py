from zad4ktesty import runtests

def falisz ( T ):

    n = len(T)
    inf = float('inf')

    DP = [[None for _ in range(n)] for _ in range(n)]
    DP[n - 1][n - 1] = 0

    def licz(x, y):

        a = inf
        b = inf

        if x < n - 1:
            a = DP[x + 1][y]

        if y < n - 1:
            b = DP[x][y + 1]

        DP[x][y] = min(a, b) + T[x][y]

    def idz(x, y):

        while True:

            licz(x, y)

            if x == 0 or y == n - 1:
                return None

            x -= 1
            y += 1

    for i in range(n - 2, -1, -1):

        idz(n - 1, i)

    for i in range(n - 2, -1, -1):

        idz(i, 0)


    return DP[0][0]

runtests ( falisz )
