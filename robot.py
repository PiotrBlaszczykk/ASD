from zad2testy import runtests
from queue import PriorityQueue

def robot(L, A, B):

    wiersze = len(L)
    kolumny = len(L[0])
    Q = PriorityQueue()

    #D: [ x ][ y ][ kierunek  ] = jak szybko sie poruszamy, im szybciej tym lepiej
    D = [[[-1 for _ in range(4)] for _ in range(kolumny)] for _ in range(wiersze)]
    wynik = [None]

    #kierunek: 0 - gora, 1 - prawo, 2 - dol, 3 - lewo
    #time, (x, y, kierunek, speed)
    Q.put((0, (A[1], A[0], 1, 60)))

    def licz(time, dane):

        x = dane[0]
        y = dane[1]
        kierunek = dane[2]
        speed = dane[3]

        if L[x][y] == "X":
            return None
        if x == B[1] and y == B[0]:
            wynik[0] = time
            return None

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

        if kierunek == 0 or kierunek == 2:

            Q.put((time + 45, (x, y, 1, 60)))
            Q.put((time + 45, (x, y, 3, 60)))

            if kierunek == 0:
                Q.put((time + speed, (x + 1, y, 0, new_speed)))

            if kierunek == 2:
                Q.put((time + speed, (x - 1, y, 2, new_speed)))

        else:

            Q.put((time + 45, (x, y, 0, 60)))
            Q.put((time + 45, (x, y, 2, 60)))

            if kierunek == 1:
                Q.put((time + speed, (x, y + 1, 1, new_speed)))

            if kierunek == 3:
                Q.put((time + speed, (x, y - 1, 3, new_speed)))


    while not Q.empty():

        czas, dane = Q.get()
        licz(czas, dane)

        if wynik[0] is not None:
            return wynik[0]

    return None

runtests(robot)
