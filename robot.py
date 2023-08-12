from zad2testy import runtests
from queue import PriorityQueue

def robot(L, A, B):

    inf = float('inf')
    wiersze = len(L)
    kolumny = len(L[0])
    Q = PriorityQueue()

    blokada = [[False for _ in range(kolumny)] for _ in range(wiersze)]

    for i in range(wiersze):
        for j in range(kolumny):
            if L[i][j] == "X":
                blokada[i][j] = True

    #D: [ x ][ y ][ kierunek  ] = jak szybko sie poruszamy, im szybciej tym lepiej
    D = [[[-1 for _ in range(4)] for _ in range(kolumny)] for _ in range(wiersze)]
    wynik = [inf]

    #kierunek: 0 - gora, 1 - prawo, 2 - dol, 3 - lewo
    #time, (x, y, kierunek, speed)
    Q.put((0, (A[1], A[0], 1, 60)))

    def licz(time, dane):

        x = dane[0]
        y = dane[1]
        kierunek = dane[2]
        speed = dane[3]
        fast = None

        if speed == 60:
            fast = 0
            new_speed = 40
        elif speed == 40:
            fast = 1
            new_speed = 30
        else:
            fast = 2
            new_speed = 30

        if D[x][y][kierunek] >= fast:
            return None
        D[x][y][kierunek] = fast


        if x == B[1] and y == B[0]:
            wynik[0] = time

        if kierunek == 0:

            if not blokada[x + 1][y]:
                Q.put((time + speed, (x + 1, y, 0, new_speed)))

            if not blokada[x][y + 1]:
                Q.put((time + 45, (x, y, 1, 60)))

            if not blokada[x][y - 1]:
                Q.put((time + 45, (x, y, 3, 60)))

        if kierunek == 1:

            if not blokada[x][y + 1]:
                Q.put((time + speed, (x, y + 1, 1, new_speed)))

            if not blokada[x + 1][y]:
                Q.put((time + 45, (x, y, 0, 60)))

            if not blokada[x - 1][y]:
                Q.put((time + 45, (x, y, 2, 60)))

        if kierunek == 2:

            if not blokada[x - 1][y]:
                Q.put((time + speed, (x - 1, y, 2, new_speed)))

            if not blokada[x][y + 1]:
                Q.put((time + 45, (x, y, 1, 60)))

            if not blokada[x][y - 1]:
                Q.put((time + 45, (x, y, 3, 60)))

        if kierunek == 3:

            if not blokada[x][y - 1]:
                Q.put((time + speed, (x, y - 1, 3, new_speed)))

            if not blokada[x + 1][y]:
                Q.put((time + 45, (x, y, 0, 60)))

            if not blokada[x - 1][y]:
                Q.put((time + 45, (x, y, 2, 60)))

        return None

    while not Q.empty():

        czas, dane = Q.get()
        licz(czas, dane)

        if wynik[0] != inf:
            return wynik[0]

    return None

runtests(robot)
