from collections import deque
from collections import Counter

def mastermindScore(g1,g2):

	if len(g1)>len(g2):
		gi,g2 = g2,g1

	print(g1)
	print(g2)
	g1_count = Counter(g1)
	g2_count = Counter(g2)
	# matching = len(set(g1) & set(g2))
	matching = sum(min(g2_count[a],b) for a,b in g1_count.items())
	print("matching ", matching)
	blacks = sum(1 for v1, v2 in zip(g1,g2) if v1 == v2)
	print("Pegs  black: {0} white {1}".format(blacks, matching-blacks))

g1 = deque()

g1.append("za")
g1.append("zs")
g1.append("mo")
g1.append("mo")
g1.append("mo")

g2 = deque()
g2.append("mo")
g2.append("we")
g2.append("zl")
g2.append("mo")
g2.append("mo")

mastermindScore(g2, g1)