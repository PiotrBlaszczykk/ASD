from zad6ktesty import runtests

def haslo ( S ):

    n = len(S)
    tab = [None for _ in range(n)]
    for i in range(n):
        tab[i] = int(S[i])

    for i in range(n - 1):
        if tab[i] == 0 and tab[i + 1] == 0:
            return 0
        if tab[i] > 2 and tab[i + 1] == 0:
            return 0

    DP = [None for _ in range(n)]

    if tab[n - 1] == 0:
        DP[n - 1] = 0
    else:
        DP[n - 1] = 1

    if tab[n - 2] == 0:
        DP[n - 2] = 0
    else:

        liczba = (tab[n - 2] * 10) + tab[n - 1]
        if liczba <= 26:
            DP[n - 2] = 2
        else:
            DP[n - 2] = 1


    def licz(index):

        if tab[index] == 0:
            DP[index] = 0
            return None

        liczba = (tab[index] * 10) + tab[index + 1]

        if liczba < 27:

            DP[index] = DP[index + 1] + DP[index + 2]

        else:
            DP[index] = DP[index + 1]

    for i in range(n - 3, -1, -1):
        licz(i)

    return DP[0]

runtests ( haslo )
