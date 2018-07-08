# Reinforcement Learning Problem
# 10*10 Grid World Problem using Value Iteration  

import math

# Grid Dimensions
global rowValue
rowValue = 10
global colValue
colValue = 10

# Positive Terminal State Reward & Dimensions
global positiveReward
positiveReward = 2.0
global rowValuePTS
rowValuePTS = 0
global colValuePTS
colValuePTS = 9

# Negative Terminal State Reward & Dimensions
global negativeReward
negativeReward = -2.0
global rowValueNTS
rowValueNTS = 1
global colValueNTS
colValueNTS = 9

# Stone Terminal State Dimensions
global rowValueSTS
rowValueSTS = 2
global colValueSTS
colValueSTS = 7



# Print Grid board
def printGridResult(grid, policyGrid, iteration):
	print ("Iteration:", iteration)
	for row in range(rowValue):
		for col in range(colValue):
			if (row == rowValueSTS) & (col == colValueSTS):
				print (policyGrid[row][col], end = "       ")
			else:
				print (grid[row][col], "(", policyGrid[row][col], ")", end = "   ")
		print ()

	print ()
	print ()



# Implement Reinforcement Learning Algorithm - Value Iteration
def valueIterationAlgorithm(grid, gridUP, row, col):
	# Reward of non-terminal state
	reward = (float(0.0))

	# Gamma value (Discount) 
	discount = (float(0.91))

	# Probability Noise = 0.15
	highProbability = (float(0.85))
	lowProbability = (float(0.075))

	resultList = []

	if (row == rowValuePTS) & (col == colValuePTS):
		return 'N'
	elif (row == rowValueNTS) & (col == colValueNTS):
		return 'N'
	elif (row == rowValueSTS) & (col == colValueSTS):
		return 'STONE'

	resultList.append((northMove(grid, row, col)*highProbability) + (westMove(grid, row, col)*lowProbability) + (eastMove(grid, row, col)*lowProbability))
	resultList.append((southMove(grid, row, col)*highProbability) + (westMove(grid, row, col)*lowProbability) + (eastMove(grid, row, col)*lowProbability))
	resultList.append((eastMove(grid, row, col)*highProbability) + (northMove(grid, row, col)*lowProbability) + (southMove(grid, row, col)*lowProbability))
	resultList.append((westMove(grid, row, col)*highProbability) + (northMove(grid, row, col)*lowProbability) + (southMove(grid, row, col)*lowProbability))

	bestResult = resultList.index(max(resultList))

	gridUP[row][col] = round((reward + (discount * resultList[bestResult])), 2)

	if(bestResult == 0):
		return 'N'
	elif(bestResult == 1):
		return 'S'
	elif(bestResult == 2):
		return 'E'
	elif(bestResult == 3):
		return 'W'



# Calculate North Move of Current State based on previous value
def northMove(grid, row, col):
	if(row == 0):
		return (float(grid[row][col]))
	elif (row == rowValueSTS+1) & (col == colValueSTS):
		return (float(grid[row][col]))
	else:
		return (float(grid[row-1][col]))



# Calculate South Move of Current State based on previous value
def southMove(grid, row, col):
	if(row == rowValue-1):
		return (float(grid[row][col]))
	elif (row == rowValueSTS-1) & (col == colValueSTS):
		return (float(grid[row][col]))
	else:
		return (float(grid[row+1][col]))



# Calculate East Move of Current State based on previous value
def eastMove(grid, row, col):
	if col == colValue-1:
		return (float(grid[row][col]))
	elif (row == rowValueSTS) & (col == colValueSTS-1):
		return (float(grid[row][col]))
	else:
		return (float(grid[row][col+1]))



# Calculate West Move of Current State based on previous value
def westMove(grid, row, col):
	if(col == 0):
		return (float(grid[row][col]))
	elif (row == rowValueSTS) & (col == colValueSTS+1):
		return (float(grid[row][col]))
	else:
		return (float(grid[row][col-1]))



# Maximum number of iteration
N = 10

# Store Grid Utilities values for each states
gridUtility = [[0.0 for x in range(colValue)] for y in range(rowValue)]

# Store Current Grid Utilities values for each states
gridUtilityPrime = [[0.0 for x in range(colValue)] for y in range(rowValue)]

# Store policy for states which is initially North for all states
policy = [['N' for x in range(colValue)] for y in range(rowValue)]


# Positive terminal state
gridUtilityPrime[rowValuePTS][colValuePTS] = positiveReward

# Negative terminal state
gridUtilityPrime[rowValueNTS][colValueNTS] = negativeReward

# Stone
gridUtilityPrime[rowValueSTS][colValueSTS] = 0.0
policy[rowValueSTS][colValueSTS] = 'STONE'

iteration = 0

printGridResult(gridUtilityPrime, policy, iteration)

while iteration < N:
	iteration += 1

	for i in range(rowValue):
		for j in range(colValue):
			gridUtility[i][j] = gridUtilityPrime[i][j]

	
	row = rowValue-1
	
	for row in reversed(range(rowValue)):
		for col in range(colValue):
			policyValue = valueIterationAlgorithm(gridUtility, gridUtilityPrime, row, col)
			policy[row][col] = policyValue
			
	printGridResult(gridUtility, policy, iteration)
