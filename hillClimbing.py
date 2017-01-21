import csv
import math
import numpy as np

def y(x):
	return float(math.cos((x**2.0) / 2.0) / np.log2(x + 2.0))

def hillClimbing(x0, deltaX, e):

	# dummy high value
	deltaY = 1000

	# Starting x and y values
	bestX = x0
	bestY = y(x0)

	print "x0: " + str('{0:.2f}'.format(bestX)) + " y0: " + str('{0:.2f}'.format(bestY)) + " deltaX: " + str('{0:.2f}'.format(deltaX))

	steps = 0

	while deltaY > e and (bestX >= 0.0 or bestX <= 10.0):

		steps += 1

		neighbour1 = bestX - deltaX
		neighbour2 = bestX + deltaX	

		neighbours = []

		if neighbour1 >= 0.0 and neighbour1 <= 10.0:
			neighbours.append(neighbour1)

		if neighbour2 >= 0.0 and neighbour2 <= 10.0:
			neighbours.append(neighbour2)

		oldBestY = bestY

		for x in neighbours:

			yVal = y(x)

			# print "x: " + str(x)
			# print "yVal: " + str(yVal)

			if yVal > bestY:
				bestY = yVal
				bestX = x

		# print "bestX: " + str(bestX)
		# print "bestY: " + str(bestY)

		deltaY = bestY - oldBestY

	return bestX, bestY, steps




def main():
	startXRange = 11
	errorThreshold = 0.00001

	deltaXList = [float(x) / 100 for x in range(1, 11)]

	results = []

	for x0 in range(startXRange):

		print("###########################################################################")

		for deltaX in deltaXList:
			
			(bestX, bestY, steps) = hillClimbing(float(x0), deltaX, errorThreshold)

			results.append([x0, deltaX, '{0:.2f}'.format(bestX), '{0:.2f}'.format(bestY), steps, errorThreshold])

			print('{0:.2f}'.format(bestX), '{0:.2f}'.format(bestY), steps)

	with open("a1q3a.csv", "wt") as f:
		writer = csv.writer(f)
		writer.writerow([ "x0", "deltaX", "bestX", "bestY", "steps", "errorThreshold" ])
		writer.writerows(results)


main()