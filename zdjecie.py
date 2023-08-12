from egzP2atesty import runtests
from collections import deque
from random import randint

#O(mn)

def partition(tab, p, r):

    index = randint(p, r)
    x = tab[index][1]

    tab[index], tab[r] = tab[r], tab[index]
    i = p - 1

    for j in range(p, r):

        if tab[j][1] <= x:
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

            return None

        elif pivot > k:

            koniec = pivot - 1
            pivot = partition(tab, pocz, koniec)

        elif pivot < k:

            pocz = pivot + 1
            pivot = partition(tab, pocz, koniec)

def zdjecie(T, m, k):

    n = len(T)
    tab = [None for _ in range(n)]
    rzedy = [None for _ in range(n)]
    m_kopia = m
    k_kopia = k

    for i in range(n):
        tab[i] = T[i]

    pointer = 0
    for i in range(k):

        for j in range(m):
            rzedy[pointer] = j
            pointer += 1

    while pointer < n:
        m_kopia -= 1
        for i in range(m_kopia):
            rzedy[pointer] = i
            pointer += 1

    kolejki = [deque() for _ in range(m)]

    for i in range(m):

        quickselect(tab, k_kopia - 1)

        for j in range(k_kopia):
            kolejki[m - i - 1].append(tab[j])

        k_kopia += 1
        tab = tab[(k_kopia - 1):]

    for i in range(n):
        T[i] = kolejki[rzedy[i]].popleft()

    return None

runtests(zdjecie, all_tests=True)
