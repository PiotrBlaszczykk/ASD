from queue import PriorityQueue

def Euler(G, start):

	#G - adj. list
	#multigraf skierowany
	#recursion-proof
	n = len(G)
	last_index = [0 for _ in range(n)]
	cycle = []
	Q = PriorityQueue()

	def DFSVisit(depth, node):

		last = last_index[node]
		# print("wchodze do node", node, "zaczynam od", last)
		if last < len(G[node]):
			k = G[node][last]
			last += 1
			last_index[node] = last
			Q.put((depth, node))
			Q.put((depth - 1, k))
			return None

		cycle.append(node)

	Q.put((0, start))
	while not Q.empty():
		depth, node = Q.get()
		DFSVisit(depth, node)

	cycle.reverse()
	return cycle
