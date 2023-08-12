from random import randint

def partition(tab, p, r):
    index = randint(p, r)
    x = tab[index]

    tab[index], tab[r] = tab[r], tab[index]
    i = p - 1

    for j in range(p, r):

        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]

    return i + 1

def quickselect(tab, k):
    n = len(tab)
    pivot = partition(tab, 0, n - 1)

    pocz = 0
    koniec = n - 1

    while True:

        if pivot == k:

            return tab[pivot]

        elif pivot > k:

            koniec = pivot - 1
            pivot = partition(tab, pocz, koniec)

        elif pivot < k:

            pocz = pivot + 1
            pivot = partition(tab, pocz, koniec)
