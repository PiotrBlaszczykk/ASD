#Piotr Błaszczyk
#
#Algorytm wykorzystuje algorytm dijkstry do szukania najkrótszej ścieżki w grafie ważonym
#Mój pomysł polega na tym, aby stworzyć dwa grafy, pierwszy graf to ten domyślny G, kiedy nie jesteśmy ścigani.
#Natomiast drugi graf, nazwany G2, to graf który powstaje wtedy, gdy obrabowaliśmy zamek i jesteśmy ścigani.
#Waga każdej krawędzi w G2 została pomnożona dwa razy oraz powiększona o r.
#Aby znaleźć rozwiązanie sprawdzamy, jaki będzie potencjalny zysk/koszt z obrabowania i-tego zamku
#Teraz to co przyspiesza mój algorytm, to skorzystanie z faktu, że algorytm dijkstry znajduje najkrótsze ścieżki
#do KAŻDEGO wierzchołka grafu. Tak więc wystarczy uruchomić dijkstre tylko 2 razy: 1 raz na grafie G bez ścigania ze
#startem w s, 2 raz na grafie G2 ze ściganiem w starcie w t.
#tablica A to najkr. ścieżki w G w starcie s, tablica B to najkrótsze ścieżki w G2 w starcie t.
#teraz jak liczymy zysk z rabunku i-tego zamku, to sumujemy koszt dotarcia bez ścigania do zamku (A[i]) oraz koszt dotarcia
#z zamku do t ( B[i] ), na koniec odejmujemy zdobyte złoto ( - V[i]).
#zatem nie musimy uruchamiać dijkstry V-razy.
#wynik to minimum z V potecnjalnych rabunków oraz z przypadku, gdy w ogóle żadnego zamku nie rabujemy
#szacownie złożoności czasowej:
#tworzymy nowy graf, wykonujemy dwie dijkstry oraz licznie zysku z V zamków
#dijktrsa ma złożoność O(ElogV), E < V^2, zatem O(ElogV) = O(V^2logV)
#liczenie zysku to O(V), tworzenie nowego grafu to E.
#Zatem złożonośc czasowa algorytmu to O(V^2logV)
#Złożoność pamięciowa to O(E + V)

from egz1Atesty import runtests
from queue import PriorityQueue


def dijkstry(G, start):

  n = len(G)
  visited = [False for _ in range(n)]
  D = [float('inf') for _ in range(n)]
  D[start] = 0
  Q = PriorityQueue()
  Q.put((0, start))

  while not Q.empty():

    curr_dist, curr_node = Q.get()

    if not visited[curr_node]:

      visited[curr_node] = True

      for neighbour, d in G[curr_node]:

        if not visited[neighbour]:

          new_dist = curr_dist + d

          if new_dist < D[neighbour]:
            D[neighbour] = new_dist
            Q.put((new_dist, neighbour))

  return D

def gold(G,V,s,t,r):

  n = len(G)

  G2 = [[] for _ in range(n)]

  for i in range(n):

    for j in range(len(G[i])):

      edge = G[i][j]

      G2[i].append((edge[0], edge[1]*2 + r))

  A = dijkstry(G, s)
  #A - bez ścigania, start w początkowym zamku
  B = dijkstry(G2, t)
  #B - będąc ścigany, start w końcowym zamku

  bez_napadu = A[t]
  wynik = float('inf')

  for i in range(n):

    rabunek = A[i] + B[i] - V[i]

    if rabunek < wynik:

      wynik = rabunek

  return min(wynik, bez_napadu)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
