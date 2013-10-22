# http://stackoverflow.com/questions/1185634/how-to-solve-the-mastermind-guessing-game

from collections import deque
from collections import namedtuple
from collections import Counter
import itertools
import os

''' #input from user
print("Hello")
var = input("Your input> ")
print("oh> ", var)
'''

''' #variacie pocet vsetkych moznosti
nieco = ["".join(item) for item in itertools.product("ČMHZBRčŽ", repeat=5)]
print(nieco)

# variacie z preddefinovaneho deque
totalColors = deque()

totalColors.append("ci")
totalColors.append("mo")
totalColors.append("hn")
totalColors.append("ze")
totalColors.append("zl")
totalColors.append("ru")
totalColors.append("ce")
totalColors.append("bi")

colorsCombination = [",".join(item) for item in itertools.product(totalColors, repeat=5)]
'''
Pegs = namedtuple('Pegs', 'black, white')
combination = namedtuple("Combination", "colors, pegs")
clear = lambda: os.system("cls")
quessedCombinations = deque()

def mastermind(colors, holes):
	return dict(
		colors = colors,
		holes = holes,
		possibleCombs = set(itertools.product(colors,repeat=holes)),
		score = mastermindScore,
		endStates = Pegs(holes, 0)
	)

def hardGame():
	return mastermind(("ci", "mo", "hn", "ze", "zl", "ru", "ce", "bi"), 5)

# compares two combinations of colors and returns Pegs
def mastermindScore(g1,g2):
	if len(g1)>len(g2):
		gi,g2 = g2,g1

	g1_count = Counter(g1)
	g2_count = Counter(g2)
	matching = sum(min(g2_count[a],b) for a,b in g1_count.items())
	blacks = sum(1 for v1, v2 in zip(g1,g2) if v1 == v2)
	return Pegs(blacks, matching-blacks)

# asks the user to insert already tested combinations
def requestTestedCombinations():
	print("-----------------------------")
	nextinput = input("Do you want add new combination? (y or n)")
	if nextinput.lower() == "n":
		return

	newCombination = True
	while newCombination:
		colorsCombination = deque()
		
		count = 5
		while count > 0:
			colorsCombination.append(input("Add new color: "))
			count-=1

		print("Combination: ", colorsCombination)
		pegs = Pegs(int(input("Black pegs: ")), int(input("White pegs: ")))
		quessedCombinations.append(combination(colorsCombination, pegs))

		nextinput = "x"
		while (nextinput.lower() != 'y' and nextinput.lower() != "n"):
			print("-----------------------------")
			nextinput = input("Do you want add new combination? (y or n)")
		if nextinput.lower() == "y":
			newCombination = True
		else:
			newCombination = False
	clear()

def printTestedCombinations():
        print()
        print("     Colors       Pegs")
        for comb in quessedCombinations:
                for color in comb[0]:
                    print(color, end = " ")
                print("::", end = " ")
                print(comb[1][0], end = " ")
                print(comb[1][1])

mastermind = hardGame()
print("Possible colors: ", mastermind["colors"])
requestTestedCombinations()
print("Possible colors: ", mastermind["colors"])
printTestedCombinations()
print()



for combination in mastermind["possibleCombs"]:
	#print("testing: ", combination)
	for quessed in quessedCombinations:
		score = mastermindScore(quessed.colors,combination)	
		if (score != quessed.pegs):
			#print("fails compare: {} {}".format(score, quessed.pegs))
			break
	else:
		print("possibilities", combination)
"""
for comb in sorted(mastermind["possibleCombs"]):
	print(comb)
"""
input()
