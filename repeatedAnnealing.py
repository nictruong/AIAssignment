import csv
import math
import numpy as np
import random

def y(x):
	return float(math.cos((x**2.0) / 2.0) / np.log2(x + 2.0))

def findRandomNeighbour(x, deltaX):

	neighbour1 = x - deltaX
	neighbour2 = x + deltaX	

	neighbours = []

	range = 0

	if neighbour1 >= 0.0 and neighbour1 <= 10.0:
		range += 1
		neighbours.append(neighbour1)

	if neighbour2 >= 0.0 and neighbour2 <= 10.0:
		range += 1
		neighbours.append(neighbour2)

	randomIndex = random.randint(0, range - 1)

	return neighbours[randomIndex]


def repeatedAnnealing(x0, deltaX, T, alpha):

	yVal = y(x0)
	yMax = y(x0)

	xVal = x0
	xMax = x0

	while T > 0.00001:

		xi = findRandomNeighbour(xVal, deltaX)
		yi = y(xi)

		if yi > yMax:
			xMax = xi
			yMax = yi

		if yi > yVal:
			xVal = xi
			YVal = yi
		else:
			p = math.exp(-(yVal - yi) / T)
			randomInt = random.uniform(0, 1)

			#print(p, randomInt)

			if randomInt <= p:
				xVal = xi
				yVal = yi

		T = T * alpha

	return xMax, yMax

def main():

	print("Started")

	startXRange = 11
	deltaXList = [ 0.01, 0.05, .01 ]

	# Temperature
	T = 10000000
	alpha = 0.80

	for x0 in range(startXRange):

		print("###########################################################################")

		for deltaX in deltaXList:

			print repeatedAnnealing(x0, deltaX, T, alpha)

main()

