from egzP9btesty import runtests
from queue import PriorityQueue


def Euler(G, start):

	#G - adj. list
	#multigraf skierowany

	n = len(G)
	last_index = [0 for _ in range(n)]
	M = [[0 for _ in range(n)] for _ in range(n)]

	for i in range(n):
		for v in G[i]:
			M[i][v] += 1

	cycle = []
	Q = PriorityQueue()

	def DFSVisit(depth, node):

		last = last_index[node]
		# print("wchodze do node", node, "zaczynam od", last)

		for k in range(last, n):

			if M[node][k] > 0:
				M[node][k] -= 1
				last = k
				last_index[node] = last
				Q.put((depth, node))
				Q.put((depth - 1, k))
				return None

		last_index[node] = last
		cycle.append(node)

	Q.put((0, start))
	while not Q.empty():
		depth, node = Q.get()
		DFSVisit(depth, node)

	cycle.reverse()
	return cycle


def dyrektor(G, R):
	n = len(G)

	for i in range(n):
		for v in R[i]:
			G[i].remove(v)

	cykl = Euler(G, 0)
	return cykl


runtests(dyrektor, all_tests=True)
