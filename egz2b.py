from egz2btesty import runtests

def parking(X,Y):

  n = len(X)
  m = len(Y)
  inf = float('inf')
  DP = [[inf for _ in range(m)] for _ in range(n)]

  #ręcznie uzupełniam DP[0]
  DP[0][0] = abs(X[0] - Y[0])
  for j in range(1, m):
    DP[0][j] = min(abs(X[0] - Y[j]), DP[0][j - 1])

  for i in range(1, n):

    minmum = [None for _ in range(m)]
    minmum[0] = DP[i - 1][0]

    for j in range(1, m):

      minmum[j] = min(minmum[j - 1], DP[i - 1][j])

    for j in range(i, m):

      #licze minimum gdy buduje i-ty budynek na j-tym parkingu

      dystans = abs(X[i] - Y[j])
      DP[i][j] = minmum[j - 1] + dystans

  return min(DP[n - 1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
