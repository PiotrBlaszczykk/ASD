def merge(A, B):

    n = len(A)
    m = len(B)
    if n == 0:
        return B
    if m == 0:
        return A
    k = m + n
    tab = [None for _ in range(k)]
    a = b = 0

    # 0 - w trakcie, 1 - doszlismy do konca A, 2 - doszlismy do konca B
    flag = 0
    for i in range(k):

        if flag == 0:

            if A[a] <= B[b]:
                tab[i] = A[a]
                a += 1
            else:
                tab[i] = B[b]
                b += 1

            if a == n:
                flag = 1
            if b == m:
                flag = 2

        elif flag == 1:
            tab[i] = B[b]
            b += 1

        else:
            tab[i] = A[a]
            a += 1

    return tab

def merge_sort(tab):

    n = len(tab)
    if n == 1 or n == 0:
        return tab

    A = merge_sort(tab[:(n//2)])
    B = merge_sort(tab[(n//2):])

    return merge(A, B)
