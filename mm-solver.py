# http://stackoverflow.com/questions/1185634/how-to-solve-the-mastermind-guessing-game

from collections import deque
from collections import namedtuple
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
	matching = len(set(g1) & set(g2))
	blacks = sum(1 for v1, v2 in itertools.izip(g1,g2) if v1 == v2)
	return Pegs(blacks, matching-blacks)

# asks the user to insert already tested combinations
def requestTestedCombinations():
	newCombination = True
	while newCombination:
		colorsCombination = deque()
		
		count = 5
		while newCombination:
			colorsCombination.append(input("Add new color: "))
			count-=1
			if count==0:
				newCombination = False 

		print("Combination: ", colorsCombination)
		pegs = Pegs(input("Black pegs: "), input("White pegs: "))
		quessedCombinations.append(combination(colorsCombination, pegs))

		nextinput = "x"
		while (nextinput.lower() != 'y' and nextinput.lower() != "n"):
			print("-----------------------------")
			nextinput = input("Do you have new combination? (y or n)")
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
printTestedCombinations()

"""
for comb in sorted(mastermind["possibleCombs"]):
	print(comb)
"""
input()
