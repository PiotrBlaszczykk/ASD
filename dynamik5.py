from zad5ktesty import runtests


def garek(A):

    inf = float('-inf')

    n = len(A)
    sumy = [[None for _ in range(n)] for _ in range(n)]
    DP = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        sumy[i][i] = A[i]
        DP[i][i] = A[i]

    for i in range(n - 1):
        for j in range(i + 1, n):
            sumy[i][j] = sumy[i][j - 1] + A[j]

    def licz(a, b):

        x = sumy[a][b]

        lewo = x - DP[a + 1][b]
        prawo = x - DP[a][b - 1]

        DP[a][b] = max(lewo, prawo)

    def idz(x, y):

        while True:

            licz(x, y)

            if y == n - 1:
                return None

            x += 1
            y += 1

    for i in range(1, n):

        idz(0, i)

    return DP[0][n - 1]


runtests(garek)
