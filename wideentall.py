from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow


def usun_liscie(node, depth, poziom):

    if depth == poziom:
        return 0

    ciecia = 0

    if node.left is not None:

        if node.x[0] < poziom:
            ciecia += 1
        else:
            ciecia += usun_liscie(node.left, depth + 1, poziom)

    if node.right is not None:

        if node.x[1] < poziom:
            ciecia += 1
        else:
            ciecia += usun_liscie(node.right, depth + 1, poziom)

    return ciecia


def wideentall( T ):

    if T.left is None and T.right is None:
        return 0

    sneed = []

    def poziomy(node, depth):

        sneed.append(depth)
        if node.left is None and node.right is None:
            return depth

        node.x = [-1, -1]

        if node.left is not None:
            lewo = poziomy(node.left, depth + 1)
            node.x[0] = lewo

        if node.right is not None:
            prawo = poziomy(node.right, depth + 1)
            node.x[1] = prawo

        return max(node.x)


    depth = poziomy(T, 0)
    tab = [0 for _ in range(depth + 1)]

    for i in range(len(sneed)):
        tab[sneed[i]] += 1

    najw = max(tab)

    for i in range(depth, -1, -1):
        if tab[i] == najw:
            poziom = i
            break

    if poziom == depth:
        return usun_liscie(T, 0, poziom)

    wynik = tab[poziom + 1]

    wynik += usun_liscie(T, 0, poziom)

    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )
