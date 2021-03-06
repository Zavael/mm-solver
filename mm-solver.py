# http://stackoverflow.com/questions/1185634/how-to-solve-the-mastermind-guessing-game

from collections import deque
from collections import namedtuple
from collections import Counter
import itertools
import os
import sys

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
	return mastermind(("bi", "ce", "ci", "hn", "mo", "ru", "ze", "zl"), 5)

def printInfo():
	print("mm-solver v1.0")
	print("Master mind game helper")
	print("-----------------------------")

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
def requestTestedCombinations(holes):
	printInfo()
	nextinput = input("Do you want add new combination? (y or n)")
	if nextinput.lower() == "n":
		return

	newCombination = True
	while newCombination:
		print("Possible colors: ", mastermind["colors"])
		colorsCombination = deque()
		
		count = holes
		while count > 0:
			color = input("Add new color: ")
			if color in mastermind["colors"]:				
				colorsCombination.append(color)
				count-=1
			else:
				print("Wrong color. See \"Possible colors\"")

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
		printInfo()
		printTestedCombinations()
		print()

def printTestedCombinations():
	print("")
	print("Added combinations:")
	print("----------------------")
	print("     Colors       Pegs")
	for comb in quessedCombinations:
		for color in comb[0]:
			print(color, end = " ")
		print("::", end = " ")
		print(comb[1][0], end = " ")
		print(comb[1][1])
	print("----------------------")

def printPossibleCombinations():
	print()
	for combination in sorted(mastermind["possibleCombs"]):
		#print("testing: ", combination)
		for quessed in quessedCombinations:
			score = mastermindScore(quessed.colors,combination)	
			if (score != quessed.pegs):
				#print("fails compare: {} {}".format(score, quessed.pegs))
				break
		else:
			print("possibilities", combination)

try:
	clear()
	mastermind = hardGame()
	requestTestedCombinations(mastermind["holes"])
	printPossibleCombinations()
	input()
except KeyboardInterrupt:
    sys.exit(0)

