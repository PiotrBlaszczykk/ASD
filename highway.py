from zad8testy import runtests

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return True


def highway( A ):

    def licz(u, v):

        l = ((A[u][0] - A[v][0])**2 + (A[u][1] - A[v][1])**2)**0.5
        czas = int(l)
        if l - czas == 0:
            return czas
        else:
            return czas + 1

    n = len(A)
    E = []

    for i in range(n):
        for j in range(i + 1, n):
            edge = licz(i, j)
            E.append((edge, i, j))

    # E: (waga, u, v)
    E.sort(key=lambda x: x[0])

    def kluska():

        V = [None for _ in range(n)]
        for i in range(n):
            V[i] = Node(i)

        tree = []

        for i in range(len(E)):
            waga, u, v = E[i]

            if union(V[u], V[v]):
                tree.append(waga)

            if len(tree) == n - 1:
                return tree[-1] - tree[0]

        return float('inf')

    wynik = float('inf')
    e = len(E) - n + 1
    for i in range(e):

        wynik = min(kluska(), wynik)
        E.pop(0)

    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )
