from zad12ktesty import runtests

def autostrada( T, k ):

    n = len(T)

    DP = [[None for _ in range(n)] for _ in range(k)]

    DP[0][0] = sum(T)
    for i in range(1, n):
        DP[0][i] = DP[0][i - 1] - T[i - 1]

    def licz(index, f):
        sumy = []
        sus = 0

        for i in range(index, n):

            sneed = DP[f - 1][i]
            sumy.append(max(sus, sneed))
            sus += T[i]

        DP[f][index] = min(sumy)


    for i in range(1, k):
        for j in range(n):
            licz(j, i)

    return DP[k - 1][0]

runtests ( autostrada,all_tests=True )
