def magiczne_piatki(tab):

    n = len(tab)

    if n == 1 or n == 2:
        return tab[0]
    elif n <= 5:

        #aby nie pozmienialo tablicy
        # arr = [None for _ in range(n)]
        # for i in range(n):
        #     arr[i] = tab[i]

        flag = True

        while flag:

            flag = False
            for i in range(n - 1):

                if tab[i + 1] < tab[i]:
                    flag = True
                    tab[i + 1], tab[i] = tab[i], tab[i + 1]

        return tab[n // 2]

    a = n // 5
    b = n % 5
    if b == 0:
        arr = [None for _ in range(a)]
    else:
        arr = [None for _ in range(a + 1)]

    for i in range(a):

        pom = [None for _ in range(5)]
        for j in range(5):
            pom[j] = tab[(i * 5) + j]

        arr[i] = magiczne_piatki(pom)

    pom = [None for _ in range(b)]
    for i in range(b):
        pom[i] = tab[(a * 5) + i]

    if b != 0:
        arr[a] = magiczne_piatki(pom)

    return magiczne_piatki(arr)

def magiczny_partition(tab, p, r):

    arr = tab[p:(r + 1)]
    x = magiczne_piatki(arr)

    for i in range(p, r + 1):
        if tab[i] == x:
            index = i
            break

    tab[index], tab[r] = tab[r], tab[index]
    i = p - 1

    for j in range(p, r):

        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]

    return i + 1
